import sys
import os
sys.path.append(os.path.dirname(__file__))

from core.mouse_controller import HumanMouseController
from ai_vision.vision_ai import VisionAI
import time

class AIBot:
    def __init__(self):
        self.mouse = HumanMouseController()
        self.vision = VisionAI()
        print("\n" + "="*60)
        print("🤖 ИИ-БОТ С ВИЗУАЛЬНЫМ РАСПОЗНАВАНИЕМ ГОТОВ")
        print("="*60 + "\n")
    
    def ask_about_screen(self, question):
        """Спроси ИИ о том, что на экране"""
        return self.vision.analyze_screen(question)
    
    def click_on_element(self, element_description):
        """ИИ находит элемент и кликает на него"""
        print(f"\n🎯 Задача: Кликнуть на '{element_description}'")
        
        coords = self.vision.find_element_coordinates(element_description)
        
        if coords:
            x, y = coords
            print(f"✅ Найдено на координатах: ({x}, {y})")
            self.mouse.human_move(x, y)
            self.mouse.human_click()
            return True
        else:
            print("❌ Элемент не найден")
            return False
    
    def do_task(self, task_description):
        """ИИ выполняет задачу по описанию"""
        plan = self.vision.execute_task_by_description(task_description)
        
        print("\n⏳ Хочешь, чтобы я выполнил этот план? (y/n)")
        # В реальном использовании можно автоматизировать
        return plan

# Примеры использования
if __name__ == "__main__":
    bot = AIBot()
    
    print("⏳ Запуск через 3 секунды...")
    print("💡 Открой любую веб-страницу или программу\n")
    time.sleep(3)
    
    # ПРИМЕР 1: Спросить что на экране
    print("\n--- ПРИМЕР 1: Анализ экрана ---")
    bot.ask_about_screen("Что ты видишь на этом экране? Опиши основные элементы.")
    
    time.sleep(2)
    
    # ПРИМЕР 2: Найти и кликнуть на элемент
    print("\n--- ПРИМЕР 2: Поиск элемента ---")
    # Замени на реальное описание элемента на твоём экране
    # bot.click_on_element("кнопка поиска")
    
    print("\n✅ Демонстрация завершена!")