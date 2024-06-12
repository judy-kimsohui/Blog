
#   
JSX

5단 분석법

JSX의 정의

고유 명사

사용 이유

문자열 템플릿

document API 사용

JSX 사용

사용 방법

JSXElement

JSXAttributes

JSXChildren

## 5단 분석법

|   |   |   |   |
|---|---|---|---|
|순서|분석|단어|내용|
|1|일반 명사|-|-|
|2|고유 명사|JSX|Javascript Syntax eXtension, 자바스크립트 문법 확장|
|3|사용 이유|JSX|JavaScript에서 XML 표현을 편리하게 사용하기 위해|
|4|사용 방법|JSX|JSXElement, JSXAttribute, JSXChildren을 사용해 XML과 유사하게 사용|
|5|다른 기술과의 비교||-|

## JSX의 정의

### 고유 명사

|   |   |
|---|---|
|JSX|Javascript Syntax eXtension, 자바스크립트 문법 확장|

JSX는 자바스크립트의 문법을 확장해 XML과 같이 사용할 수 있게 하는 확장형 문법입니다.

보통은 개발자들이 리액트를 통해 JSX를 처음 접하게 되다 보니, 리액트에서만 JSX가 사용이 가능한 줄 알고 있지만 JSX는 독립적으로도 사용이 가능합니다.

JSX는 ECMAScript의 표준이 아니기 때문에, 그대로 실행하면 자바스크립트 런타임이 해석할 수 없습니다. 그렇기 때문에, 트랜스 파일러를 통해 JavaScript로 변환되어 실행해야 합니다.

## 사용 이유

|   |   |
|---|---|
|JSX|JavaScript에서 XML 표현을 편리하게 사용하기 위해|

JSX를 사용하면 자바스크립트에서 XML을 편리하게 표현할 수 있습니다.

기존 JavaScript에서 XML을 표현하거나, DOM을 조작하려면 문자열 템플릿을 사용하거나, document API를 사용해야 했습니다. 다음은 새로운 엘리먼트를 추가하는 방법을 각각 예시를 통해 알아보도록 하겠습니다.

### 문자열 템플릿

const element = `<div><p>Hello World</p></div>` document.body.innerHTML(element);

JavaScript

복사

### document API 사용

function addDivision(){ const elementDiv = document.createElement('div'); const elementP = document.createElement('p'); elementP.innerHTML = 'Hello World'; elementDiv.appendChild(elementP); document.body.appendChild(elementDiv); }

JavaScript

복사

두 방법 모두 DOM을 조작해 새로운 엘리먼트를 생성할 방법이지만 상대적으로 관리하기 어렵거나 코드가 너무 길어 직관적이지 않습니다.

JSX를 사용하면 간단하게 다음과 같이 변경할 수 있습니다.

### JSX 사용

const AddDivision = () => ( <div> <p>Hello World</p> </div> );

JavaScript

복사

보기에 직관적으로 변경되고 각 엘리먼트를 사용하는 방법 또한 기존 HTML과 유사하게 사용할 수 있습니다.

## 사용 방법

|   |   |
|---|---|
|JSX|JSXElement, JSXAttribute, JSXChildren을 사용해 XML과 유사하게 사용|

JSX는 XML과 유사한 JSXElement, JSXAttribute, JSXChildren를 사용해 작성합니다. 기존 XML을 알고 있다면 학습하는데 큰 어려움이 없을 겁니다.

### JSXElement

// opning - closing <AddDivision></AddDivision> // self-closing <AddDivision /> // fragment <></>

JavaScript

복사

JSX를 구성하는 기본 요소입니다. 이는 HTML의 element와 비슷한 역할을 하며, 태그로 동작하게 됩니다. 태그로 동작하는 만큼, opening, closing, self-closing의 특징을 가지게 됩니다. 특이한 점으로 아무것도 없는 fragment 요소를 사용할 수 있습니다.

function hi(text){ return <div> hi {text}</div> } export function App(){ // 정상 실행되지 않음. return <hi text={"world!"}/> }

JavaScript

복사

주의할 점은 JSX Element의 요소 명은 대문자로 시작해야 합니다. JSX 특성상 기존 HTML의 element를 사용할 수 있는데, 소문자로 태그 명이 시작하게 되면 JSX는 해당 태그를 HTML 태그로 인식해 정상적으로 실행되지 않습니다.

### JSXAttributes

function Hello(props){ return <div>{props.name} {props.age}</div> } export function App(){ return <> <Hello name={"foo"} age={30}/> <Hello { ...{name : 'bar', age: 20} }/> </> }

JavaScript

복사

JSX에 부여할 수 있는 속성을 의미합니다. 이는 선택 값 이기 때문에, 사용하지 않아도 문제없습니다. 값은 키와 값 쌍으로 전달할 수 있으며, JavaScript 전개 연산자도 사용이 가능합니다.

function Child(props){ return <div>{props.attribute}</div> } export function App(){ return ( <div> <Child attribute={<div>hi</div>}/> </div> ) }

JavaScript

복사

JSX Element또한 JSX Attribute로 들어갈 수 있습니다. 하지만 문법적 가독성 문제로 잘 사용되지는 않습니다.

### JSXChildren

function ComponentA(){ return <div></div> } function ComponentB(){ return <div></div> } export function A(){ return ( <ComponentA> <ComponentB /> </ComponentA> ) }

JavaScript

복사

JSX Element의 자식 요소를 표현합니다. HTML의 자식 요소를 표현하는 것과 유사하게 작성됩니다.

Today

1

- 1초 전