import random

class HumanBehavior:
    """Имитация человеческого поведения"""
    
    @staticmethod
    def reaction_time():
        """Время реакции человека (0.2-0.8 сек)"""
        return random.uniform(0.2, 0.8)
    
    @staticmethod
    def thinking_pause():
        """Пауза на размышление (0.5-2.5 сек)"""
        return random.uniform(0.5, 2.5)
    
    @staticmethod
    def should_make_mistake():
        """Человек промахивается в 5% случаев"""
        return random.random() < 0.05
    
    @staticmethod
    def micro_pause():
        """Микропаузы (0.05-0.15 сек)"""
        return random.uniform(0.05, 0.15)
    
    @staticmethod
    def speed_variation():
        """Вариация скорости движения"""
        return random.uniform(0.7, 1.3)