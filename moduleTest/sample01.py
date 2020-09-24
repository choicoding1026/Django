'''
1) module
    - python file( *.py)
    - 
2) package
    - 서로 관련된 모듈 묶음
    -
==> 모듈이 다르면 접근 불가
    접근할 수 있도록 import 처리
    
# 외부 파일 접근 방법
    1) 경로 지정1
        import 패키지명.모듈명
    2) 경로 지정2
        from 패키지명 import 모듈명

python은 다른 프로그램 언어의  main과 같은 기능의 함수가 없다.
따라서 각 모듈이 독립적으로 실행가능
 if __name__ == "__main__":
     pass

'''
import one.other as xxx
from two.theOther import size

if __name__ == "__main__":
    pass


print(xxx.num)
print(size)

