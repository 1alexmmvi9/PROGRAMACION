import pyautogui
import base64
import os
from openai import OpenAI
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

class VisionAI:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        print("🤖 ИИ с визуальным распознаванием запущен")
    
    def take_screenshot(self, region=None):
        """Делает скриншот экрана"""
        if region:
            screenshot = pyautogui.screenshot(region=region)
        else:
            screenshot = pyautogui.screenshot()
        
        # Сохраняем во временный файл
        screenshot.save("temp_screenshot.png")
        return "temp_screenshot.png"
    
    def encode_image(self, image_path):
        """Конвертирует изображение в base64 для отправки в API"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def analyze_screen(self, instruction):
        """
        ИИ анализирует экран и отвечает на вопрос
        instruction - что ты хочешь узнать о экране
        """
        print(f"\n👁️ ИИ анализирует экран...")
        print(f"📝 Инструкция: {instruction}")
        
        # Делаем скриншот
        screenshot_path = self.take_screenshot()
        
        # Кодируем изображение
        base64_image = self.encode_image(screenshot_path)
        
        # Отправляем в GPT-4 Vision
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": instruction
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=500
        )
        
        answer = response.choices[0].message.content
        print(f"🤖 Ответ ИИ: {answer}\n")
        
        # Удаляем временный файл
        os.remove(screenshot_path)
        
        return answer
    
    def find_element_coordinates(self, element_description):
        """
        ИИ ищет элемент на экране и возвращает примерные координаты
        element_description - описание элемента (например: "красная кнопка Submit")
        """
        print(f"\n🔍 ИИ ищет: {element_description}")
        
        screenshot_path = self.take_screenshot()
        base64_image = self.encode_image(screenshot_path)
        
        # Получаем размер экрана
        screen_width, screen_height = pyautogui.size()
        
        instruction = f"""
        На этом скриншоте найди: {element_description}
        
        Размер экрана: {screen_width}x{screen_height}
        
        Ответь ТОЛЬКО в таком формате:
        X: [число]
        Y: [число]
        Уверенность: [высокая/средняя/низкая]
        
        Где X и Y - примерные координаты центра элемента в пикселях.
        Если элемент не найден, напиши: "Не найден"
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": instruction},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=100
        )
        
        answer = response.choices[0].message.content
        print(f"🤖 Результат: {answer}")
        
        os.remove(screenshot_path)
        
        # Парсим координаты
        try:
            lines = answer.split('\n')
            x = None
            y = None
            
            for line in lines:
                if 'X:' in line:
                    x = int(''.join(filter(str.isdigit, line)))
                if 'Y:' in line:
                    y = int(''.join(filter(str.isdigit, line)))
            
            if x and y:
                return (x, y)
            else:
                return None
        except:
            return None
    
    def execute_task_by_description(self, task_description):
        """
        ИИ выполняет задачу по текстовому описанию
        Например: "Нажми на кнопку Login" или "Заполни поле Email"
        """
        print(f"\n🎯 Задача: {task_description}")
        
        screenshot_path = self.take_screenshot()
        base64_image = self.encode_image(screenshot_path)
        
        screen_width, screen_height = pyautogui.size()
        
        instruction = f"""
        Задача: {task_description}
        Размер экрана: {screen_width}x{screen_height}
        
        Проанализируй скриншот и опиши пошаговый план действий.
        Укажи координаты элементов, с которыми нужно взаимодействовать.
        
        Формат ответа:
        1. Действие: [описание]
           Координаты: X=[число], Y=[число]
        2. Действие: [описание]
           Координаты: X=[число], Y=[число]
        ...
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": instruction},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=500
        )
        
        plan = response.choices[0].message.content
        print(f"\n📋 План действий:\n{plan}")
        
        os.remove(screenshot_path)
        
        return plan