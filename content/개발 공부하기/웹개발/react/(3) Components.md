
#   
Components

5단 분석법

컴포넌트의 정의

일반 명사

고유 명사

사용 이유

사용 방법

Props

State

클래스형 컴포넌트

기본 생성

props, state 구성

생명주기 (life cycle)

render() - 마운트, 업데이트 시

componentDidMount() - 마운트 직후

componentDidUpdate() - 업데이트 직후

componentWillUnMount() - 언마운트 직전

shouldComponentUpdate() - 업데이트 직전

함수형 컴포넌트

생명주기 메서드가 없다.

직관적인 코드 구성

## 5단 분석법

|   |   |   |   |
|---|---|---|---|
|순서|분석|단어|내용|
|1|일반 명사|Component|독립적으로 작동하며 재사용 가능한 개별 구성 요소|
|2|고유 명사|Component|React에서 UI를 구성하는 재사용 가능한 독립적인 코드 블록|
|3|사용 이유|Component|코드의 재사용성과 관리 효율성을 높이기 위해 사용|
|4|사용 방법|Component|JSX를 사용하여 컴포넌트를 정의하고 props와 state로 관리|
|5|다른 기술과의 비교||-|

## 컴포넌트의 정의

### 일반 명사

|   |   |
|---|---|
|Component|독립적으로 작동하며 재사용 가능한 개별 구성 요소|

컴포넌트는 독립적으로 작동하며 재사용할 수 있는 개별 구성 요소라는 뜻을 가지고 있습니다. 이는 이해하기 어려울 수 있으나 현실 세계의 레고를 생각하면 매우 쉽게 이해할 수 있습니다.

![](https://oopy.lazyrockets.com/api/v2/notion/image?src=https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fcf024025-486d-4514-84ae-3a7c5951c17c%2Fe6818f2d-1c91-4f5f-8a73-530827826b15%2FUntitled.png&blockId=17552fe1-f733-415d-b5de-dd747150daf9)

레고 블록을 생각해 보면 각 블록은 자체적으로 완전한 형태를 갖추고 있으며, 다른 블록과 결합하여 다양한 형태의 구조물을 만들 수 있습니다.

예를 들어, 단일 레고 블록 하나만으로는 작은 조각에 불과하지만, 여러 개의 블록을 서로 다른 방식으로 조합하면, 집, 자동차, 성 등과 같은 복잡한 구조를 만들어 낼 수 있습니다.

각 블록은 고유의 결합 포인트를 가지고 있어서, 다른 블록과 정확하게 맞물릴 수 있습니다. 이러한 방식으로, 레고 블록은 각각의 컴포넌트가 모여 더 크고 기능적인 구조를 형성하게 됩니다.

### 고유 명사

|   |   |
|---|---|
|Component|React에서 UI를 구성하는 재사용 가능한 독립적인 코드 블록|

리액트에서 컴포넌트는 UI를 구성하는 재사용 가능한 독립적인 코드 블록을 의미합니다. 앞서 설명해 드린 레고 블록처럼 재사용할 수 있는 작은 단위의 UI를 만들어 조합해 하나의 페이지를 만들어 낼 수 있는 방식을 의미합니다.

## 사용 이유

|   |   |
|---|---|
|Component|코드의 재사용성과 관리 효율성을 높이기 위해 사용|

이러한 컴포넌트의 특성을 잘 살린 방식의 예시를 보도록 하겠습니다.

[![](https://oopy.lazyrockets.com/api/v2/notion/image?src=https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fcf024025-486d-4514-84ae-3a7c5951c17c%2F9e6ab8f4-bc21-4f48-a713-d457f4fc1aa2%2FUntitled.png&blockId=f9a341f5-4468-4c82-8591-593631c4e4a6)](https://blog2.streamloan.io/)

다음 사진은 리액트의 디자인 패턴 중 ATOMIC 패턴의 원리를 잘 설명 해둔 이미지입니다.

작은 단위의 컴포넌트를 만들어서 관리를 편하게 해주고, 컴포넌트끼리 조합해 나가면, 최종적으로 페이지가 나오게 되어 코드의 재사용성이 증가하게 됩니다.

하지만 해당 방식을 프로젝트에 꼭 적용해야 할 필요는 없습니다. 해당 방식은 구조를 철저히 지키는 만큼 유연성 부족과 높은 학습 난이도가 단점으로 꼽히고 있습니다.

## 사용 방법

|   |   |
|---|---|
|component|JSX를 사용하여 컴포넌트를 정의하고 props와 state로 관리|

리액트의 컴포넌트는 JSX를 사용하여 컴포넌트를 정의하고 props와 state로 관리합니다.

우선 컴포넌트의 구조를 알기 전에 props와 state를 알아보도록 하겠습니다.

### Props

// props는 객체로 전달되며, 해당 코드에서는 { name="foo", age:30 }의 값이 전달 된다. function Children(props){ return <div>{props.name}</div> } export function App(){ return( <Children name={"foo"} age={30}/> ) }

JavaScript

복사

함수형 컴포넌트 props 예시

Props는 properties를 줄인 표현으로 컴포넌트의 속성을 설정할 때 사용하는 요소입니다. props는 해당 컴포넌트를 사용하는 부모 컴포넌트에서 요솟값을 할당할 수 있습니다.

### State

function Children(){ const [count,setCount] = useState(0); return ( <button onClick={() => setCount(count++)}> {count} </button> ) }

JavaScript

복사

함수형 컴포넌트 state 예시

리액트의 state는 컴포넌트의 상태를 추적하고 사용자 인터페이스(UI)를 동적으로 업데이트하기 위해 사용되는 데이터입니다.

이 데이터는 주로 사용자와의 상호작용이나 시간의 경과에 따라 변경될 수 있는 정보를 포함합니다.

React에서는 state를 사용하여 데이터의 변경에 반응하여 UI를 제 렌더링합니다.

State의 사용 방법은 Class 형 컴포넌트와 Function 형 컴포넌트에서 각각 다르게 사용됩니다.

### 클래스형 컴포넌트

클래스형 컴포넌트는 현재에는 함수형 컴포넌트의 등장으로 잘 사용하지 않는 방식이 되었지만, 16.8 이전 버전에서는 클래스 컴포넌트가 주를 이루었습니다.

이러한 역사가 짧지 않기 때문에, 비교적 최근 사용을 시작한 함수형 컴포넌트만 배우는 것이 아닌, 클래스형 컴포넌트에 대해서도 이해하고 있어야 합니다.

클래스형 컴포넌트를 이해하고 있으면 함수형 컴포넌트에 대한 이해는 매우 쉽게 이해할 수 있습니다.

#### 기본 생성

import React from 'react' class SampleComponent extends React.Component{ render(){ return <h1> Hello, World! </h1> } }

JavaScript

복사

클래스형 컴포넌트를 생성할 때는 원하는 클래스를 우선 생성한 뒤, React.Component를 확장해 줍니다.

render() 메소드

사용자에게 보일 화면을 구성하는 함수입니다. 이전에 배웠던 XML 문법을 통해 JSX Element를 구성할 수 있습니다.

#### props, state 구성

import React from 'react' class SampleComponent extends React.Component{ constructor(props){ super(props) this.state = { count : 0 } } handleClick = () => { const newValue = this.state.count + 1 this.setState({ count: newValue }) } render() { const { props : {text}, state : {count} } = this return ( <button onClick={this.handleClick}> {count} </button> ) } }

JavaScript

복사

class 컴포넌트의 props, state 구성 및 메소드 작성 방법

클래스 컴포넌트는 생성자(contructor)를 통해 props와 state를 컨트롤할 수 있습니다.

super은 상속받은 컴포넌트(React.Component)의 생성자를 호출해 전달받은 props를 사용할 수 있게 해 줍니다.

state의 경우 this binding을 통해 생성자에서 초기화 후 사용하게 됩니다.

#### 생명주기 (life cycle)

![](https://oopy.lazyrockets.com/api/v2/notion/image?src=https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fcf024025-486d-4514-84ae-3a7c5951c17c%2Fed1edc84-db70-47cd-9e2b-2f227b396474%2FUntitled.png&blockId=bbe6eb68-cdb8-4070-8235-d7377f74fd47)

클래스 컴포넌트는 생명주기를 가지고 있습니다. 생명주기란 컴포넌트의 생성부터 소멸까지 발생하는 일련의 이벤트를 말합니다.

이러한 생명주기는 여러 단계로 나뉘며, 각 단계에서는 특정 코드를 실행할 수 있습니다.

이를 통해 컴포넌트가 화면에 렌더링 되기 전, 렌더링 된 후, 업데이트되고, 마지막으로 제거될 때 개발자가 특정 이벤트를 실행할 수 있는 환경을 제공하고 있습니다.

우선 생명주기는 크게 3가지로 나눌 수 있습니다.

•

마운트 (mount)

◦

컴포넌트가 생성되는 시점

•

업데이트 (update)

◦

이미 생성된 컴포넌트의 내용이 변경되는 시점.

•

언마운트 (unmount)

◦

컴포넌트를 더 이상 사용하지 않아 제거하는 시점.

#### render() - 마운트, 업데이트 시

렌더 메서드는 클래스 생명 주기 중 유일하게 필수 요소로 들어가 있습니다.

렌더 함수는 순수 함수로 동작해야 합니다. 이는 렌더 함수 내부에서 setState와 같이 상태를 변경하면 안 된다는 뜻입니다.

이렇게 순수하게 유지하는 이유는, 렌더 함수에서 직접 state를 업데이트하면 side-effect가 발생할 확률이 매우 높으며, 유지보수가 어려워 집니다.

#### componentDidMount() - 마운트 직후

메서드 이름에서 알 수 있듯이, 컴포넌트가 마운트 된 직후 호출되는 메서드 입니다. 해당 메서드에서는 setState를 호출할 수 있는데, 이 경우 render 메서드가 한 번 더 호출됩니다.

다만 실제 DOM에 적용되기 전에 render 메서드가 호출되기 때문에 사용자는 알 수 없습니다.

#### componentDidUpdate() - 업데이트 직후

![](https://oopy.lazyrockets.com/api/v2/notion/image?src=https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fcf024025-486d-4514-84ae-3a7c5951c17c%2F2fdc4af0-b32f-4138-9e1a-a3ede7aa8321%2FUntitled.png&blockId=cdaaec75-1d8d-47c8-9386-d40465357597)

state, props의 변화가 생긴다면 호출되는 메서드 입니다.

해당 메서드에서 setState와 같이 상태를 변화해도 되지만, 잘못 사용하면 무한 반복에 빠지게 됩니다.

만약 state를 업데이트하고 싶다면 적절하게 조건문을 통해 작성해 주어야 합니다.

#### componentWillUnMount() - 언마운트 직전

컴포넌트가 더 이상 사용되지 않아 제거되기 직전에 호출되는 메서드입니다. 해당 메서드에서는 setState를 호출할 수 없으며, 일반적으로 클린업 함수를 호출하기 위해 사용됩니다.

componentWillUnmount() { document.removeEventListner('resize', this.resizeEvent); }

JavaScript

복사

클린업 함수란 주로 컴포넌트의 생명주기에서 컴포넌트가 DOM에서 제거되기 전에 수행되는 작업을 말합니다.

이 함수는 컴포넌트와 관련된 리소스를 정리하고, 메모리 누수를 방지하기 위해 사용됩니다.

예를 들어, 이벤트 리스너를 제거하거나, 네트워크 요청을 취소하거나, 타이머를 정지시키는 등의 작업이 이에 해당합니다.

#### shouldComponentUpdate() - 업데이트 직전

state나 props가 업데이트되기 직전 호출되는 생명주기 메서드입니다. 해당 메서드의 반환 값은 true, false 값을 반환함 으로서, true면 업데이트 이후 render() 메서드가 호출최 리 렌더링이 발생합니다.

만약 업데이트하고 싶지 않다면 해당 메서드에서 false를 리턴하도록 작성해 주면 됩니다.

shouldComponentUpdate(nextProps, nextState){ let isUpdate = false // something.. return isUpdate }

JavaScript

복사

이러한 클래스형 컴포넌트는 잘 다룬다면 온전한 애플리케이션을 만드는데 큰 무리가 없습니다. 그렇다면 왜 함수형 컴포넌트가 등장 했고, 주목받고 있을까요?

기존 클래스형 컴포넌트는 작성해야 할 코드가 많아 자바스크립트 번들 파일이 커지고, 학습 난도를 높였습니다.

마치 우리가 스마트폰을 사용하는데, 모든 기능을 사용하지는 않지만, 핸드폰은 점점 더 고사양으로 더 많은 기능을 탑재하는 형태로 발전한 것과 같습니다.

그래서 함수형 컴포넌트는 필수적인 기능은 모두 넣되, 최대한 가볍게 사용할 수 있도록 제작이 되어 있습니다.

### 함수형 컴포넌트

함수형 컴포넌트는 최근 새롭게 등장한 개념이 아닌 초창기 리액트 버전부터 있던 기능입니다. 하지만 16.8버전 이후 함수형 컴포넌트에서 사용할 수 있는 hook이 도입되면서 주목받고 있습니다.

import React from 'react' class SampleComponent extends React.Component{ constructor(props){ super(props) this.state = { count : 0 } } handleClick = () => { const newValue = this.state.count + 1 this.setState({ count: newValue }) } render() { const { props : {text}, state : {count} } = this return ( <button onClick={this.handleClick}> {count} </button> ) } }

JavaScript

복사

클래스형 컴포넌트

import { useState } from 'react' export function SampleComponent(props) { const [count, setCount] = useState(0); function handleClick(){ const newValue = count + 1; setCount(newValue) } return ( <button onClick={handleClick}> {count} </button> ) }

JavaScript

복사

함수형 카운터 예제

클래스형 컴포넌트에서 함수형 컴포넌트로 동일한 기능을 구현해 보았습니다. 간단한 코드이지만 매우 간결해진 것을 확인할 수 있습니다.

그렇다면 함수형 컴포넌트는 클래스형 컴포넌트와 무엇이 다른 걸까요?

#### 생명주기 메서드가 없다.

생명주기 메서드는 React.Component의 기능이기 때문에 상속을 받지 않는 함수형은 사용할 수 없습니다.

이를 대체하기 위해서 useEffect hook을 사용해서 비슷하게 구현할 수 있습니다.

이후 hook을 상세히 다룰 때 이야기를 자세히 하겠지만, 이로써 기존 클래스형보다 쉽고 간결하게 코드를 작성할 수 있게 되었습니다.

#### 직관적인 코드 구성

클래스형 컴포넌트는 상속의 개념을 사용하기 때문에 Class 문법에 익숙 하다면 강력하게 사용할 수 있습니다. 하지만 코드 자체가 직관적이지 않고 학습 난도가 높습니다.

함수형 컴포넌트의 경우 기존 자바스크립트 개발자들이 사용하던 방식을 그대로 채용했으며, state 관리 또한 hook을 사용하고 있어 더욱 간결하게 사용할 수 있게 합니다.

Today

1

- 0초 전