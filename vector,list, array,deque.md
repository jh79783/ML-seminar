# std::vector

- vector는 대표적인 시퀀스 컨테이너이며, 임의의 접근 반복자(random access iterator)를 지원하는 배열 기반 컨테이너입니다.

  > 시퀀스 컨테이너(sequence container) : 특별히 삽입과 삭제의 규칙이 존재하지 않는 컨테이너
  >
  > 반복자(iterator) : 컨테이너에 저장되어있는 원소를 참조할 때 사용. 포인터와 비슷한 객체.
  >
  > 임의의 접근 반복자(random access iterator) : 양방향 반복자 기능에 +, -, ++, --, +=,, -=, [], <, >, <=, >=, ==, != 연산이 가능한 반복자(vector, deque)
  >
  > 양방향 반복자(bidirectional iterator) : 순방향 반복자 기능에 역방향으로 이동(--)이 가능한 반복자(list, set, multiset, map, multimap), =, ==, ++, --연산 가능
  >
  > 순방향 반복자(forward iterator) : 입력, 출력 반복자 기능에 순방향으로 이동(++)이 가능한 재할당 될 수 있는 반복자
  >
  > 입력 반복자(input iterator) : 현 위치의 원소를 한번만 읽을 수 있는 반복자(istream)
  >
  > 출력 반복자(output iterator) : 현 위치의 원소를 한번만 쓸 수 있는 반복자(ostream)

  vector와 단순한 배열과의 다른점은 배열의 크기를 미리 정하지 않고 필요에 따라 배열의 길이가 정해지는 것입니다.
  간단히 말해 자동으로 메모리가 할당되는 배열이라고 할 수 있습니다. 즉 동적길이배열입니다.
  개별 원소에 접근하기 용이하며, 어떠한 순서로도 원소들을 순회할 수 있습니다.
  하지만 새로운 원소가 추가될때마다 메모리 재할당과 이전 원소 복사가 있어 성능이 저하될 수 있습니다.

  > 메모리 삭제 -> 메모리 할당 -> 원소 복사

vector의 선언은 다음과 같이 합니다.

```cpp
vector<data type>[name];
ex) vector<int> v;
```

## vector의 생성자

- vector v;

  비어있는 vector v를 생성합니다.

- vector v(n);

  크기가 n인 vector v를 생성합니다. (모든 벡터요소 0으로 초기화)

- vector v(n, x);

  x의 값을 가지고 크기가 n인 vector v를 생성합니다.

- vector v2(v1);

  v1 vector를 복사해 v2를 생성합니다.

또한 vector는 '==', '!=', '<', '>', '<=', '>=' 연산자를 사용하여 대소 비교가 가능합니다.

>vector <int\>v[] = {{1, 2}, {3, 4}}
>
>- 벡터 배열 생성 (행은 가변 열은 고정)
>
>vector<vector<int\>> v
>
>- 2차원 벡터 생성(행과 열 모두 가변)

## vector의 멤버함수

vector<int\> v;로 가정합니다.

- v.assign(n, x);

  x의 값으로 n개의 원소를 할당합니다.

- v.at(idx);

  idx번째 원소를 참조합니다.

  v[idx]보다 느리지만 안전합니다.

  > 범위를 확인합니다.

- v(idx);

  idx번째 원소를 참조합니다.

  v.at[idx]보다 빠릅니다.

- v.front();

  첫번째 원소를 참조합니다.

- v.back();

  마지막 원소를 참조합니다.

- v.size();

  원소의 개수를 리턴합니다.

- v.capacity();

  할당된 공간의 크기를 리턴합니다.

- v.clear();

  모든 원소를 제거합니다.

  **원소를 제거하지만 메모리 자체는 남아있습니다.**

  size는 줄어들고 capacity는 그대로입니다.

  - size는 실제 유효한 요소의 갯수입니다.
  - capacity는 메모리에 할당되어 요소를 담을 수 있는 공간의 용량입니다.

- v.push_back(x);

  마지막 원소 뒤에 x값을 추가합니다.

- v.pop_back();

  마지막 원소를 제거합니다.

- p = v.begin();

  첫번째 원소를 가리키는 반복자입니다.

  - ex) for(p=v.begin(); p!=v.end(); p++)

- p = v.end();

  마지막 원소의 다음을 가리키는 반복자입니다.

- p = v.rbegin();

  끝에서 첫번째 원소를 가리키는 반복자입니다.

- p = v.rend();

  끝에서 마지막 원소를 가리키는 반복자입니다.

- v.reserve(n);

  n개의 원소를 저장할 위치 예약합니다.(미리 동적 할당)

- v.resize(n, x)

  크기를 n으로 변경합니다(10 -> 5로 줄이면 짤리는가).

  확장되는 공간을 x값으로 초기화합니다.

- v.swap(v2);

  v와 v2의 모든것(요소와 메모리)를 서로 바꿔줍니다.

- q = v.insert(idx, x);

  idx위치에 x값을 삽입한다.

  q는 삽입한 원소를 가리키는 반복자입니다.

- v.insert(idx, x, n);

  idx위치에 x값을 n개 삽입합니다.

- v.empty();

  vector가 비어있다면 true를 리턴해줍니다.

  비어있는 기준은 size가 0일때입니다.

  capacity하고 상관이 없습니다.

- v.erase(idx) or v.erase(star_idx, end_idx)
  원하는 index값의 요소를 지웁니다.

- v.emplace(idx, x)
  원하는 위치에 요소를 삽입합니다.

- v.emplace_back(x)
  벡터의 마지막 부분에 새로운 요소를 추가합니다.

## push_back VS emplace_back

함수 원형

- push_back

  - void push_back( const T& value );

    - 값 복사를 통한 요소 추가

  - void push_back( T&& value );    //C++11

    > R-Value 개념

    - (임시)객체의 복사가 아닌 이동을 통한 요소 추가 

  > 즉 push_back같은 삽입 함수는 삽입할 객체를 받음

- emplace_back

  - void emplace_back( Args&&... args );
    - 삽입할 객체의 생성자를 위한 인자를 받아 삽입

  > 즉 emplace_back같은 생성 삽입 함수는 삽입할 객체의 생성자들을 위한 인자들을 받아 **vector 내에서 직접** 객체를 생성하여 삽입한다. 따라서 임시 객체의 **생성과 파괴, 복사(또는 move)**를 하지 않아도 됨

push_back은 삽입하기위해 객체를 만들어 전달하고 내부적으로 다시 임시 객체를 만듭니다.
하지만 emplace_back은 생성에 필요한 인자를 내부에서 생성 삽입합니다.

```cpp
#include<iostream>
#include<string>
#include<vector>

class PEB{

protected:
    int Index;
    std::string strName;
    int n;

public:
    PEB(const int Index, const std::string& strName, const int n)
        : Index(Index)
        , strName(strName)
        , n(n)
    {
        std::cout<<strName<<" 생성자 호출"<<std::endl;
    }

    PEB(PEB&I)
        : Index(I.Index)
        , strName(move(I.strName))
        , n(I.n)
    {
        std::cout<<strName<<"복사 생성자 호출"<<std::endl;
    }

    PEB(PEB&&I)
        : Index(I.Index)
        , strName(move(I.strName))
        , n(I.n)
    {
        std::cout<<strName<<"이동 생성자 호출"<<std::endl;
    }

    ~PEB(){
        std::cout<<strName<<" 소멸자 호출"<<std::endl;
    }

};

int main(){
    std::vector<PEB> Push_Emplace;

    Push_Emplace.emplace_back(0,"emplace_back", 10);
//    Push_Emplace.push_back(PEB(5, "push_back", 5));

    return 0;
}

//결과
emplace_back 생성자 호출
emplace_back 소멸자 호출

push_back 생성자 호출			// 객체 생성
push_back이동 생성자 호출		   // 내부적으로 임시 객체 생성
 소멸자 호출						
push_back 소멸자 호출
```



## R-Value

C++ 에서의 Lvalue와 Rvalue은 L과 R은 Left, Right를 의미하지 않습니다.
Lvalue : 표현식이 종료된 이후에도 없어지지 않고 지속되는 개체 (예: 모든 변수)
Rvalue : 표현식이 종료되면 더이상 존재하지 않는 임시적인 개체 (예: 상수, 임시 객체)
Rvalue와 Lvalue를 확인하는 방법은 &를 붙여 에러가 난다면 Rvalue라고 할 수 있습니다.
하지만 이 &는 Lvalue참조자 이기때문에 C++11에서는 Rvalue Reference가 추가되었습니다.

> Lvalue Reference = &
> Rvalue Reference = &&

하지만 Rvalue는 Rvalue Reference와 같은 것은 아닙니다.



## 예제

```cpp
#include<iostream>
#include<string>
#include<vector>

int main(){
    std::cout<<"생성"<<std::endl;
    std::vector<int> v;
    for(int i=0; i<10; i++){
        v.push_back(i+1);
        std::cout<<"v[i]:"<<v[i]<<", "<<"v.size():"<<v.size()<<", "<<"v.capacity():"<<v.capacity()<<std::endl;
    }

    std::cout<<"다양한 접근법"<<std::endl;
    std::vector<int> v1;
    v1.push_back(5);
    v1.push_back(8);
    v1.push_back(53);
    v1.push_back(22);
    for(int i=0; i<v1.size(); i++){
        std::cout<<"at:"<<v1.at(i)<<" ";
        std::cout<<"[]:"<<v1[i]<<" ";
    }
    std::cout<<std::endl;
    std::vector<int>::iterator iter;
    for(iter=v1.begin(); iter!=v1.end(); iter++){
        std::cout<<*iter<<" ";
    }
    std::cout<<std::endl;

    std::cout<<"삽입, 삭제"<<std::endl;
    std::vector<std::string> name;
    name.push_back("썬콜");
    name.push_back("아크");
    name.push_back("히어로");
    name.push_back("아델");
    std::cout<<"name.front():"<<name.front()<<std::endl;
    std::cout<<"name.back():"<<name.back()<<std::endl;

   /*std::vector<std::string>::iterator iter1;
    for(iter1=name.begin();iter1!=name.end();iter1++){
        std::cout<<*iter1<<"/";
    }
    
    name.pop_back();
    
    for(iter1=name.begin();iter1!=name.end();iter1++){
         std::cout<<*iter1<<"/";
    }
    
    for(iter1=name.begin();iter1!=name.end();iter1++){
         if(*iter1=="아크"){
             name.erase(iter1);
             break;
         }
    }
    
     for(iter1=name.begin();iter1!=name.end();iter1++){
         std::cout<<*iter1<<"/";
    }*/

    for(auto iter1=name.begin(); iter1!=name.end(); iter1++)
        std::cout<<*iter1<<"/";
    std::cout<<std::endl;

    name.pop_back();

    for(auto iter1=name.begin(); iter1!=name.end(); iter1++)
        std::cout<<*iter1<<"/";

    std::cout<<std::endl;

    for(auto iter1=name.begin(); iter1!=name.end(); iter1++){
        if(*iter1=="아크"){
            name.erase(iter1);
            break;
        }
    }

    for(auto iter1=name.begin(); iter1!=name.end(); iter1++)
        std::cout<<*iter1<<"/";
    std::cout<<std::endl;
    std::cout<<name.empty()<<" "<<name.size()<<" "<<name.capacity()<<std::endl;
    name.clear();
    std::cout<<name.empty()<<" "<<name.size()<<" "<<name.capacity()<<std::endl;

    return 0;
}

//결과
생성
v[i]:1, v.size():1, v.capacity():1
v[i]:2, v.size():2, v.capacity():2
v[i]:3, v.size():3, v.capacity():4
v[i]:4, v.size():4, v.capacity():4
v[i]:5, v.size():5, v.capacity():8
v[i]:6, v.size():6, v.capacity():8
v[i]:7, v.size():7, v.capacity():8
v[i]:8, v.size():8, v.capacity():8
v[i]:9, v.size():9, v.capacity():16
v[i]:10, v.size():10, v.capacity():16
다양한 접근법
at:5 []:5 at:8 []:8 at:53 []:53 at:22 []:22 
5 8 53 22 
삽입, 삭제
name.front():썬콜
name.back():아델
썬콜/아크/히어로/아델/
썬콜/아크/히어로/
썬콜/히어로/
0 2 4
1 0 4
```



## auto

C++11 이전에는 auto는 자동 저장소 클래스에 있는 변수, 지역변수를 선언하는 역할을 했었습니다.

> 저장소 클래스 : typedef, static ...등 정보를 어떤 저장소에 보관할지 지정해주는 예약어

하지만 C++11부터는 auto는 선언의 초기화식에서 형식이 추론되는 변수를 선언하는 역할을 하고 있습니다.

```cpp
// ex1)
#include<iostream>

int main(){
    // initializer_list<int>
    auto A = {1, 2};
    // initializer_list<int>
    auto B = {3};
    // int
    auto C = 5;
    // double
    auto D = 5.4;
    std::cout<<"자료형:"<<typeid(A).name()<<std::endl;
    std::cout<<"자료형:"<<typeid(B).name()<<std::endl;
    std::cout<<"자료형:"<<typeid(C).name()<<std::endl;
    std::cout<<"자료형:"<<typeid(D).name()<<std::endl;
}

//결과
자료형:St16initializer_listIiE
자료형:St16initializer_listIiE
자료형:i
자료형:d
```



# std::deque

deque는 vector와 마찬가지로 배열로써 작동하며 vector의 단점을 보완하기 위해 만들어 졌습니다.
원소를 컨테이너의 시작과끝에서 삽입/제거가 가능합니다. 하지만 시작/끝이 아닌 지점에서 삽입/제거는 list에 비해 떨어집니다. 또한 컨테이너가 연속 메모리 공간이 아니기 때문에 원소들간의 포인터 연산이 불가능해 집니다.

> 포인터 연산 : 포인터 변수에 +, -, ++, -- 를 사용하는 것

deque는 여러개의 메모리 블록을 할당하고 하나의 블록처럼, 취급합니다.
![](https://bduvenhage.me/assets/images/deque.png)

메모리가 부족할 때마다 새로운 메모리 블록을 할당하기 때문에 이전 원소를 복사하지 않습니다.

deque의 선언은 다음과 같습니다.

```cpp
deque<data type>[name];
ex) deque<int> dq;
```

## deque의 생성자

vector의 생성자, 멤버함수와 90%이상 일치합니다.

- deque dq;

  비어있는 dq를 생성합니다.

- deque dq(n);

  0으로 초기화된 n개의 원소를 갖는 dq를 생성합니다.

- deque dq(n, x);

  x로 초기화된 n개의 원소를 갖는 dq를 생성합니다.

- deque dq2(dq1);

  dq1를 복사하여 dq2를 생성합니다.

vector와 마찬가지로 연산자를 사용하여 대소비교가 가능합니다.

## deque의 멤버함수

deque<int\> dq 로 가정합니다.

- dq.push_front(x);

  dq의 첫번째 원소 앞에 원소 x를 삽입합니다.

- dq.pop_front();

  dq의 첫번째 원소를 제거합니다.

- dq.push_back(x);

  dq의 마지막 원소 뒤에 원소 x를 삽입합니다.

- dq.pop_back();

  dq의 마지막 원소를 제거합니다.

- dq.capacity();

  존재하지 않습니다.

나머지는 vector의 멤버함수와 동일합니다.



# std::array

vector는 앞서 동적 길이 배열이라고 하였는데 array는 이와 반대되는 고정 길이 배열입니다.

array의 선언은 다음과 같습니다.

```cpp
array<data type, size> [name];
```

고정 길이이기 때문에 배열의 크기를 지정해주어야 합니다.

일반적인 배열과 array container의 차이점 중 한가지는 대입 연산자가 사용이 가능하단 점입니다.

```cpp
std::array<int, 3> a = {1, 2, 3};
std::array<int, 3> b;

b = a;  // b 에 {1,2,3} 이 들어간다

int arr[3] = {1, 2, 3};
int b[3];

b = arr;  // 불가능
```



## array의 생성자

- array<int, 3> arr1 = {1, 2, 3};

  크기 3, 초기화값 1,2,3

- array<int, 3> arr1;

  크기3, 쓰레기값

- array<int, 3> arr1 = {0};

  크기3, 모든 원소값 0

- array<int,3> arr1 = {1};

  크기3, 첫번째 원소값만 1 나머지 원소값은 0

## array의 멤버함수

- arr.begin();

  배열의 맨 첫번째 원소를 가리킵니다.

  반복자 입니다.

- arr.end();

  배열의 맨 마지막 **다음**원소를 가리키는 반복자 입니다. 

  > 마지막 원소 + 1

- arr.rbegin();

  배열을 거꾸로했을때 맨 첫번째 원소입니다.

  > 즉 맨 마지막 원소

  반복자 입니다.

- arr.rend();

  배열을 거꾸로했을때 마지막 다음원소를 가리킵니다.

  반복자 입니다.

  > 즉 첫 번째 원소 - 1

- arr.cbegin();, arr.cend();

  위와 동일하지만 const가 붙어서 iterator를 사용해 원소를 수정할 수 없습니다.

- arr.crbegin();, arr.crend();

  위와 동일합니다.

- arr.front()

  맨 앞의 원소를 반환합니다.

- arr.back()

  맨 뒤의 원소를 반환합니다.

- arr.data()

  배열의 포인터를 반환합니다.(배열의 첫번째 원소의 주소)

- arr.fill(val)

  배열의 인자를 val값으로 전부 바꿉니다.

- arr.swap(arr2)

  arr2의 인자와 arr의 인자를 스왑합니다.

  길이와 타입이 같아야  합니다.

- arr.at(n)

  n번째 인자를 반환합니다.

- arr[n]

  n번째 인자를 반환합니다.

- arr.empty()

  비어있는지 확인합니다.

- arr.max_size()

  배열의 최대 사이즈를 반환합니다. (size와 같음)

- arr.size()

  배열의 사이즈를 반환합니다. (max_size와 같음)
  
  > 배열은 초기화하면서 채워지기때문에 배열크기와 같은 값 반환

## 예제

```cpp
#include<iostream>
#include<array>

int main(){
    std::array<int, 3> arr1 = {1,5,6};
    std::array<int, 5> arr2 = {0};
    std::array<int, 8> arr3;
    std::cout<<"size "<<"max_size "<<std::endl;
    std::cout<<arr1.size()<<" "<<arr1.max_size()<<std::endl;
    std::cout<<arr2.size()<<" "<<arr2.max_size()<<std::endl;
    std::cout<<arr3.size()<<" "<<arr3.max_size()<<std::endl;

    std::cout<<"front & back"<<std::endl;
    std::cout<<arr1.front()<<" "<<arr1.back()<<std::endl;

    std::cout<<"fill & swap"<<std::endl;
    std::cout<<"default"<<" "<<arr1[0]<<" "<<arr1[1]<<" "<<arr1[2]<<std::endl;
    arr1.fill(90);
    std::cout<<"fill"<<" "<<arr1[0]<<" "<<arr1[1]<<" "<<arr1[2]<<std::endl;
    std::array<int, 3> swap1 = {80, 100, 800};
    arr1.swap(swap1);
    std::cout<<"swap"<<" "<<arr1[0]<<" "<<arr1[1]<<" "<<arr1[2]<<std::endl;
}

//결과
size max_size 
3 3
5 5
8 8
front & back
1 6
fill & swap
default 1 5 6
fill 90 90 90
swap 80 100 800
```





# std::list

list는 노드 기반 컨테이너로써 이중 연결 리스트 구조입니다.
이중 연결 리스트는 모든 노드가 이전 노드와 다음 노드에 대한 정보를 모두 저장하고 있는 리스트를 의미합니다.

![](https://t1.daumcdn.net/cfile/tistory/210D54415838361D23)

위와 같은 그림으로 표현할 수 있습니다.



앞의 vector와 다르게 list는 정렬과 이어붙이기가 있으며, at과[]를 이용하여 탐색은 불가능하고 --또는++를 이용하여 탐색을 할 수 있습니다. 또한 컨테이너의 어느 위치에서도 삽입/제거가 빠르고 순서의 이동 또한 빠릅니다.
하지만 특정 원소에서의 접근이 불가능 합니다.

> 특정 원소에 접근하기 위해 처음이나 끝에서 부터 선형 탐색이 요구
>
> 선형 탐색 : 처음부터 끝까지 하나씩 순서대로 비교하여 원하는 값을 찾아내는 알고리즘

list의 선언은 다음과 같습니다.

```cpp
list<data type>[name];
ex)list<int> lt1;
```

## list의 생성자

- list lt

  비어있는 lt를 생성합니다.

- list lt(n)

  0으로 초기화된 n개의 원소를 생성합니다.

- list lt(n,x)

  x값으로 초기화된 n개의 원소를 생성합니다.

- list lt1(lt)

  lt를 lt1로 복사하여 생성합니다.

list도 마찬가지로 크기비교 연산자를 사용할 수 있습니다.

## list의 멤버함수

list<int\> lt 로 가정합니다.

- 앞서 설명한 vector와 비슷한 사용법

  - lt.assig(n,x)
  - lt.front()
  - lt.back()
  - lt.begin()
  - lt.end()
  - lt.rbegin()
  - lt.rend()
  - lt.push_back(x)

  뒤쪽으로 x값을 삽입합니다.

- lt.push_front(x)

  앞으로 x값을 삽입합니다.

- lt.pop_back()

  맨 마지막 원소를 제거합니다.

- lt.pop_front()

  맨 앞의 원소를 제거합니다.

- lt.inert(iter,x)

  iter가 가르키는 위치에 원소 x를 삽입합니다.

  삽입한 원소를 가르키는 iterator를 반환합니다.

- lt.eraser(iter)

  iter가 가르키는 원소를 삭제합니다.

  삭제한 다음 원소를 가르키는 iterator를 반환합니다.

- lt.size()

- lt.remove(x)

  x와 같은 원소를 모두 삭제합니다.

- lt.remove_if(Predicate)

  단항 조건자 predicate에 해당하는 원소를 모두 제거합니다.

- lt.reverse()

  원소들의 순서를 뒤집습니다.

- lt.sort()

  모든 원소를 오름차순으로 정렬합니다.

  파라미터값으로 이항 조건자가 올 수 있으며, 이때는 조건자 기준으로 정렬합니다.

- lt2.swap(lt1)

- lt1.splice(iter2, lt1)

  lt2에서 iter2가 가리키는 곳에 lt1의 모든 원소를 붙입니다.

  lt2.splice(iter2, lt1, iter1) : lt2에 iter2가 가리키는 곳에 lt1의 iter1이 가리키는 원소를 붙입니다.

  lt2.splice(iter2, lt1, iter1_1, iter1_2) : lt2에 iter2가 가리키는 곳에 lt1의 iter1_1~iter1_2까지의 원소를 붙입니다. 이때 범위는 [liter1_1, iter1_2)입니다.

- lt.unique()

  인접한(양옆) 원소가 같으면 하나를 남기고 모두 삭제합니다.

- lt2.merge(lt1)

  lt1을 lt2내부로 합엽하여 오름차순으로 정렬합니다.

  파라미터로 이항 조건자가 올 수 있으며 이때 조건자를 기준으로 정렬합니다.

## 예제

```cpp
#include<iostream>
#include<list>
#include<string>
bool pre(int num){
    return num==100;
}
int main(){
    std::list<int> lt;
    lt.push_back(10);
    lt.push_back(40);
    lt.push_back(80);
    lt.push_back(90);
    lt.push_back(100);
    lt.push_back(120);
    lt.push_back(150);
    lt.push_back(100);
    std::list<int>::iterator iter;
    std::cout<<"original: "<<std::endl;
    for(iter=lt.begin();iter!=lt.end();iter++){
        std::cout<<*iter<<" ";
    }
    std::cout<<std::endl;

    std::cout<<"remove_if"<<std::endl;
    lt.remove_if(pre);
    for(iter=lt.begin();iter!=lt.end();iter++){
        std::cout<<*iter<<" ";
    }
    std::cout<<std::endl;
    std::cout<<std::endl;


    std::list<std::string> lt2;
    lt2.push_back("l");
    lt2.push_back("h");
    lt2.push_back("r");
    lt2.push_back("y");
    lt2.push_back("z");
    lt2.push_back("o");
    lt2.push_back("o");
    lt2.push_back("o");
    lt2.push_back("q");
    std::list<std::string>::iterator iter2;
    std::cout<<"original string"<<std::endl;
    for(iter2=lt2.begin();iter2!=lt2.end();iter2++){
        std::cout<<*iter2<<" ";
    }
    std::cout<<std::endl;
    lt2.sort();
    std::cout<<"sort"<<std::endl;
    for(iter2=lt2.begin();iter2!=lt2.end();iter2++){
        std::cout<<*iter2<<" ";
    }
    std::cout<<std::endl;
    std::cout<<"unique"<<std::endl;
    lt2.unique();
    for(iter2=lt2.begin();iter2!=lt2.end();iter2++){
        std::cout<<*iter2<<" ";
    }
    std::cout<<std::endl;
    std::cout<<std::endl;



    std::list<std::string> st1;
    std::list<std::string> st2;
    st1.push_back("a");
    st1.push_back("b");
    st1.push_back("c");
    st1.push_back("d");
    st2.push_back("Q");
    st2.push_back("W");
    st2.push_back("E");
    std::list<std::string>::iterator siter;
    std::cout<<"original_st1: ";
    for(siter=st1.begin();siter!=st1.end();siter++){
        std::cout<<*siter<<" ";
    }
    std::cout<<"original_st2: ";
    for(siter=st2.begin();siter!=st2.end();siter++){
        std::cout<<*siter<<" ";
    }
    std::cout<<std::endl;

    siter = st2.begin();
    siter++;
    st2.splice(siter, st1);
    std::cout<<"splice: ";
    for(siter=st2.begin();siter!=st2.end();siter++){
        std::cout<<*siter<<" ";
    }
    
}

//결과
original: 
10 40 80 90 100 120 150 100 
remove_if
10 40 80 90 120 150 

original string
l h r y z o o o q 
sort
h l o o o q r y z 
unique
h l o q r y z 

original_st1: a b c d original_st2: Q W E 
splice: Q a b c d W E 
```

