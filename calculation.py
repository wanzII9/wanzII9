import math
from typing import List, Tuple, Union, Optional
from datetime import datetime


class AdvancedCalculator:
    """
    고급 계산기 클래스
    다양한 수학 연산과 계산 히스토리 기능을 제공합니다.
    """
    
    def __init__(self):
        """계산기 초기화"""
        self.history: List[Tuple[str, float, datetime]] = []
        self.operations = {
            '+': ('덧셈', lambda x, y: x + y),
            '-': ('뺄셈', lambda x, y: x - y),
            '*': ('곱셈', lambda x, y: x * y),
            '/': ('나눗셈', lambda x, y: x / y if y != 0 else None),
            '**': ('제곱', lambda x, y: x ** y),
            '%': ('나머지', lambda x, y: x % y if y != 0 else None),
            'sqrt': ('제곱근', lambda x, y: math.sqrt(x)),
            'log': ('로그', lambda x, y: math.log(x, y) if x > 0 and y > 0 and y != 1 else None),
            'sin': ('사인', lambda x, y: math.sin(math.radians(x))),
            'cos': ('코사인', lambda x, y: math.cos(math.radians(x))),
            'tan': ('탄젠트', lambda x, y: math.tan(math.radians(x)))
        }
    
    def display_welcome(self) -> None:
        """환영 메시지와 사용 가능한 연산자 표시"""
        print("=" * 50)
        print("🎯 고급 계산기에 오신 것을 환영합니다!")
        print("=" * 50)
        print("\n📋 사용 가능한 연산자:")
        for op, (name, _) in self.operations.items():
            print(f"  {op:>6} : {name}")
        print("\n💡 특별 기능:")
        print("  'history' : 계산 히스토리 보기")
        print("  'clear'   : 히스토리 지우기")
        print("  'quit'    : 종료")
        print("=" * 50)
    
    def get_number(self, prompt: str) -> Optional[float]:
        """사용자로부터 숫자 입력 받기"""
        while True:
            try:
                user_input = input(prompt).strip()
                if user_input.lower() in ['quit', 'exit', 'q']:
                    return None
                return float(user_input)
            except ValueError:
                print("❌ 잘못된 입력입니다. 숫자를 입력해주세요.")
    
    def get_operation(self) -> Optional[str]:
        """사용자로부터 연산자 입력 받기"""
        while True:
            op = input("\n🔢 연산자를 입력하세요: ").strip()
            if op.lower() in ['quit', 'exit', 'q']:
                return None
            if op in self.operations:
                return op
            elif op.lower() == 'history':
                self.show_history()
                continue
            elif op.lower() == 'clear':
                self.clear_history()
                continue
            else:
                print(f"❌ 지원하지 않는 연산자입니다: {op}")
                print("✅ 지원하는 연산자:", ', '.join(self.operations.keys()))
    
    def calculate(self, num1: float, op: str, num2: Optional[float] = None) -> Optional[float]:
        """계산 수행"""
        if op not in self.operations:
            print(f"❌ 지원하지 않는 연산자: {op}")
            return None
        
        op_name, operation_func = self.operations[op]
        
        try:
            # 단항 연산자 처리
            if op in ['sqrt', 'sin', 'cos', 'tan']:
                result = operation_func(num1, 0)  # num2는 사용하지 않음
            else:
                if num2 is None:
                    print("❌ 이 연산에는 두 번째 숫자가 필요합니다.")
                    return None
                result = operation_func(num1, num2)
            
            if result is None:
                print("❌ 계산할 수 없습니다. (예: 0으로 나누기, 음수의 제곱근 등)")
                return None
            
            # 히스토리에 추가
            if op in ['sqrt', 'sin', 'cos', 'tan']:
                expression = f"{op}({num1})"
            else:
                expression = f"{num1} {op} {num2}"
            
            self.history.append((expression, result, datetime.now()))
            
            return result
            
        except Exception as e:
            print(f"❌ 계산 중 오류가 발생했습니다: {e}")
            return None
    
    def show_history(self) -> None:
        """계산 히스토리 표시"""
        if not self.history:
            print("\n📝 계산 히스토리가 비어있습니다.")
            return
        
        print("\n📝 계산 히스토리:")
        print("-" * 50)
        for i, (expression, result, timestamp) in enumerate(self.history[-10:], 1):  # 최근 10개만 표시
            print(f"{i:2d}. {expression} = {result}")
            print(f"    시간: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
    
    def clear_history(self) -> None:
        """계산 히스토리 지우기"""
        self.history.clear()
        print("🗑️ 계산 히스토리가 지워졌습니다.")
    
    def run(self) -> None:
        """계산기 실행"""
        self.display_welcome()
        
        while True:
            print("\n" + "=" * 30)
            
            # 첫 번째 숫자 입력
            num1 = self.get_number("첫 번째 숫자를 입력하세요: ")
            if num1 is None:
                break
            
            # 연산자 입력
            op = self.get_operation()
            if op is None:
                break
            
            # 두 번째 숫자 입력 (필요한 경우)
            num2 = None
            if op not in ['sqrt', 'sin', 'cos', 'tan']:
                num2 = self.get_number("두 번째 숫자를 입력하세요: ")
                if num2 is None:
                    break
            
            # 계산 수행
            result = self.calculate(num1, op, num2)
            
            if result is not None:
                op_name = self.operations[op][0]
                if op in ['sqrt', 'sin', 'cos', 'tan']:
                    print(f"\n✅ {op_name}({num1}) = {result}")
                else:
                    print(f"\n✅ {num1} {op} {num2} = {result}")
                print(f"📊 결과: {result}")
            
            # 계속할지 묻기
            continue_calc = input("\n🔄 다른 계산을 하시겠습니까? (y/n): ").strip().lower()
            if continue_calc not in ['y', 'yes', 'ㅇ']:
                break
        
        print("\n👋 계산기를 사용해주셔서 감사합니다!")
        if self.history:
            print(f"📈 총 {len(self.history)}개의 계산을 수행했습니다.")


def main():
    """메인 함수"""
    calc = AdvancedCalculator()
    calc.run()


if __name__ == "__main__":
    main()
