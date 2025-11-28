"""
Модуль для публикации результатов спортсменов в Google Таблицу.
Работает через сервисный аккаунт, не требует интерактивного входа.
"""

import json
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GoogleSheetsPublisher:
    """Публикация результатов в Google Таблицу."""

    def __init__(self, config_path: str = "config.json"):
        """
        Инициализирует соединение с Google Таблицей.
        :param config_path: Путь к config.json
        """
        self.config = self._load_config(config_path)
        self.service = self._authenticate()
        self.spreadsheet_id = self.config["spreadsheet_id"]
        self.sheet_name = self.config["sheet_name"]

    def _load_config(self, path: str) -> Dict[str, Any]:
        """Загружает конфиг из JSON-файла."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.critical(f"Файл конфигурации не найден: {path}")
            raise
        except json.JSONDecodeError as e:
            logger.critical(f"Ошибка парсинга config.json: {e}")
            raise

    def _authenticate(self) -> Any:
        """Аутентификация через сервисный аккаунт."""
        try:
            credentials = Credentials.from_service_account_file(
                self.config["credentials_path"],
                scopes=["https://www.googleapis.com/auth/spreadsheets"]
            )
            # УБРАТЬ ПРОВЕРКУ НА refresh_token (ошибка из-за отсутствия атрибута)
            # Обновление токена, если нужно (для сервисного аккаунта обычно не требуется)
            if not credentials.valid:
                try:
                    credentials.refresh(Request())
                except Exception as e:
                    logger.error(f"Ошибка при обновлении токена: {e}")
                    raise
            service = build("sheets", "v4", credentials=credentials)
            logger.info("Аутентификация в Google Sheets прошла успешно.")
            return service
        except Exception as e:
            logger.critical(f"Ошибка аутентификации: {e}")
            raise

    def publish_results(
        self,
        cup: str,
        category: str,
        sportsmen: List[Dict[str, Any]],
        total_column: str = "Итог",
        timestamp: Optional[str] = None
    ) -> bool:
        """
        Публикует результаты спортсменов в Google Таблицу.
        :param cup: Название турнира
        :param category: Категория
        :param sportsmen: Список словарей с данными спортсменов
        :param total_column: Название столбца с итогом (по умолчанию "Итог")
        :param timestamp: Дата/время вручную (по умолчанию — текущее)
        :return: True, если успешно
        """
        if not sportsmen:
            logger.warning("Список спортсменов пуст. Публикация пропущена.")
            return False

        # Формат времени
        if not timestamp:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Данные для записи
        values = []
        for i, sport in enumerate(sportsmen, start=2):  # Строка 1 — заголовки
            row = [
                timestamp,
                cup,
                category,
                sport.get("name", ""),
                sport.get("point_1", ""),
                sport.get("point_2", ""),
                sport.get("point_3", ""),
                sport.get("point_4", ""),
                sport.get("point_5", ""),
                sport.get("point_6", ""),
                sport.get("penalty", ""),
                sport.get("total", "")
            ]
            values.append(row)

        # Заголовки
        header = [
            "Дата/Время",
            "Турнир",
            "Категория",
            "Спортсмен",
            "Оценка 1",
            "Оценка 2",
            "Оценка 3",
            "Оценка 4",
            "Оценка 5",
            "Оценка 6",
            "Штраф",
            "Итог"
        ]

        # Объединяем заголовки и данные
        body = {
            "values": [header] + values
        }

        # Путь к листу
        range_name = f"{self.sheet_name}!A1"

        try:
            result = self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=range_name,
                valueInputOption="USER_ENTERED",
                body=body
            ).execute()

            logger.info(f"Успешно опубликовано {result.get('updates').get('updatedCells')} ячеек.")
            return True

        except HttpError as error:
            logger.error(f"Ошибка при публикации в Google Таблицу: {error}")
            return False

    def test_connection(self) -> bool:
        """Проверяет подключение к таблице."""
        try:
            result = self.service.spreadsheets().get(spreadsheetId=self.spreadsheet_id).execute()
            logger.info(f"Подключение к таблице '{result.get('properties').get('title')}' успешно.")
            return True
        except Exception as e:
            logger.error(f"Ошибка подключения: {e}")
            return False


# === Пример использования ===
if __name__ == "__main__":
    # Пример данных
    test_data = [
        {
            "name": "Иванов И.И.",
            "point_1": 8.5,
            "point_2": 9.0,
            "point_3": 8.7,
            "point_4": 8.8,
            "point_5": 8.6,
            "point_6": 8.9,
            "penalty": 0.5,
            "total": 52.0
        },
        {
            "name": "Сидоров А.В.",
            "point_1": 9.1,
            "point_2": 9.2,
            "point_3": 9.0,
            "point_4": 8.9,
            "point_5": 9.3,
            "point_6": 9.0,
            "penalty": 0.0,
            "total": 54.5
        }
    ]

    # Инициализация
    publisher = GoogleSheetsPublisher()

    # Проверка подключения
    if not publisher.test_connection():
        print("❌ Не удалось подключиться к Google Таблице.")
    else:
        # Публикация
        success = publisher.publish_results(
            cup="Чемпионат города",
            category="Юниоры",
            sportsmen=test_data,
            total_column="Итог"
        )
        if success:
            print("✅ Результаты успешно опубликованы в Google Таблицу.")
        else:
            print("❌ Ошибка публикации.")
