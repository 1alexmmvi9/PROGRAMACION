import pyautogui
import random
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from detection_evasion.bezier_curves import BezierTrajectory
from core.human_behavior import HumanBehavior

pyautogui.FAILSAFE = True

class HumanMouseController:
    def __init__(self):
        self.action_count = 0
        print("✅ Контроллер мыши запущен")
        print("⚠️ Для остановки: переместите мышь в левый верхний угол экрана")
    
    def human_move(self, x, y):
        """Движение мыши как человек"""
        print(f"🖱️ Двигаюсь к ({x}, {y})")
        
        time.sleep(HumanBehavior.reaction_time())
        
        current_pos = pyautogui.position()
        
        trajectory = BezierTrajectory.generate_bezier_curve(
            current_pos, 
            (x, y),
            control_points=random.randint(1, 3)
        )
        
        for point in trajectory:
            jitter_x = random.randint(-2, 2)
            jitter_y = random.randint(-2, 2)
            
            final_x = point[0] + jitter_x
            final_y = point[1] + jitter_y
            
            speed_factor = HumanBehavior.speed_variation()
            duration = 0.001 * speed_factor
            
            pyautogui.moveTo(final_x, final_y, duration=duration)
            
            if random.random() < 0.1:
                time.sleep(HumanBehavior.micro_pause())
        
        if HumanBehavior.should_make_mistake():
            print("   ❌ Промах! Исправляю...")
            offset_x = random.randint(-10, 10)
            offset_y = random.randint(-10, 10)
            pyautogui.moveTo(x + offset_x, y + offset_y, duration=0.1)
            time.sleep(0.1)
            pyautogui.moveTo(x, y, duration=0.1)
        
        print(f"   ✅ Достигнута позиция")
        self.action_count += 1
    
    def human_click(self, x=None, y=None):
        """Клик как человек"""
        if x is not None and y is not None:
            self.human_move(x, y)
        
        print("🖱️ Кликаю...")
        
        time.sleep(HumanBehavior.reaction_time() * 0.5)
        
        click_duration = random.uniform(0.05, 0.15)
        
        pyautogui.mouseDown()
        time.sleep(click_duration)
        pyautogui.mouseUp()
        
        time.sleep(HumanBehavior.micro_pause())
        
        print("   ✅ Клик выполнен")
        self.action_count += 1