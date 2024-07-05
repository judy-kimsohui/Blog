### Spring Framework와 Spring Boot 사용 이유

#### 1. EJB의 불편함과 Spring의 장점

**EJB (Enterprise JavaBeans):**
- EJB는 Java EE의 구성 요소로, 분산 시스템에서의 비즈니스 로직을 쉽게 구현하기 위해 사용됩니다.
- 하지만, EJB는 다음과 같은 이유로 불편하다고 평가됩니다:
  - **복잡한 설정:** XML 설정 파일과 같은 복잡한 설정이 필요합니다.
  - **무거운 컨테이너:** EJB를 실행하기 위해 무거운 애플리케이션 서버가 필요합니다.
  - **개발 생산성 저하:** EJB의 복잡성으로 인해 개발 속도가 느려질 수 있습니다.

**Spring Framework:**
- **경량 프레임워크:** Spring은 경량이며, 설정이 간단합니다.
- **POJO 기반 개발:** Spring은 Plain Old Java Object(POJO)를 사용하여 객체지향적인 개발을 촉진합니다.
- **유연한 의존성 주입:** Spring은 다양한 방법으로 의존성을 주입할 수 있습니다.
- **모듈화:** 필요에 따라 Spring의 다양한 모듈을 선택하여 사용할 수 있습니다.

#### 2. Spring Boot 사용 이유

**Spring Boot:**
- **빠른 시작:** 복잡한 설정 없이 빠르게 애플리케이션을 시작할 수 있습니다.
- **자동 구성:** Spring Boot는 대부분의 설정을 자동으로 구성해 줍니다.
- **내장 서버:** 별도의 애플리케이션 서버 없이 내장 Tomcat, Jetty 등을 사용할 수 있습니다.
- **스타터 패키지:** 필요한 의존성을 쉽게 추가할 수 있는 스타터 패키지를 제공합니다.

### 객체지향과 느슨한 연결 (Loose Coupling)

**느슨한 연결:**
- 구현체와 인터페이스를 분리하여 코드의 유연성과 재사용성을 높입니다.
- 인터페이스를 통해 구현체를 교체하기 쉬워집니다.

**다형성:**
- 자바 언어의 다형성을 활용하여 다양한 구현체를 동일한 인터페이스로 사용할 수 있습니다.
- 인터페이스 설계를 잘 하면 코드의 확장성과 유지보수성이 향상됩니다.

### Spring과 다형성, 객체지향

**Spring의 다형성 적용:**
- Spring은 다형성을 적극 활용합니다. 예를 들어, `@Autowired`를 통해 인터페이스를 주입받아 다양한 구현체를 사용할 수 있습니다.
- Spring의 의존성 주입(DI)을 통해 객체지향적인 설계를 쉽게 구현할 수 있습니다.

### Spring Container와 Bean

**Spring Container:**
- Spring 컨테이너는 빈의 생명주기를 관리합니다.
- 빈(Bean)은 Spring 컨테이너가 관리하는 객체입니다.

**빈의 생명주기:**
1. **빈 인스턴스화(Instantiation):** 빈 객체가 생성됩니다.
2. **의존성 주입(Dependency Injection):** 필요한 의존성이 주입됩니다.
3. **초기화(Initialization):** 초기화 작업이 수행됩니다.
4. **사용(Usage):** 빈이 사용됩니다.
5. **소멸(Destruction):** 빈이 소멸됩니다.

### Spring Boot의 DI와 IoC

**DI (Dependency Injection):**
- DI는 객체 간의 의존성을 주입하여 결합도를 낮춥니다.
- Spring Boot에서는 `@Autowired`, `@Inject`, `@Resource` 등을 사용하여 의존성을 주입할 수 있습니다.

**IoC (Inversion of Control):**
- IoC는 객체의 생성과 의존성 관리를 컨테이너가 대신 수행하는 디자인 패턴입니다.
- Spring은 IoC 컨테이너를 통해 객체의 생명주기와 의존성을 관리합니다.

### Spring Boot의 기본적인 사용법

**의존성 주입 (DI):**
- `@Autowired` 어노테이션을 사용하여 의존성을 주입할 수 있습니다.
- 예시:
  ```java
  @Service
  public class MyService {
      private final MyRepository myRepository;
      
      @Autowired
      public MyService(MyRepository myRepository) {
          this.myRepository = myRepository;
      }
  }
  ```

### Spring Container와 Embedded Web Server

**Spring Container:**
- Spring Container는 빈의 생명주기를 관리하고 의존성을 주입합니다.

**Embedded Web Server:**
- Spring Boot는 내장 웹 서버를 제공하여 별도의 애플리케이션 서버 없이도 웹 애플리케이션을 실행할 수 있습니다.

### Annotation 사용 방법

**어노테이션:**
- Spring에서는 다양한 어노테이션을 사용하여 설정과 기능을 간편하게 관리할 수 있습니다.
- 예시:
  - `@Component`, `@Service`, `@Repository`: 빈으로 등록
  - `@Autowired`: 의존성 주입
  - `@Configuration`: 설정 클래스

### 빈 수집 과정과 자동 설정

**빈 수집 과정:**
- Spring은 클래스패스를 스캔하여 빈을 자동으로 수집합니다.
- `@ComponentScan` 어노테이션을 사용하여 특정 패키지를 스캔할 수 있습니다.

**자동 설정 (Auto Configuration):**
- Spring Boot는 자동 설정을 통해 대부분의 설정을 자동으로 구성해 줍니다.
- `@EnableAutoConfiguration` 어노테이션을 사용하여 자동 설정을 활성화할 수 있습니다.

### Spring Boot의 웹 살펴보기

**Spring Boot와 Express.js 비교:**
- **Spring Boot:** 자바 기반, 강력한 의존성 관리와 풍부한 기능 제공
- **Express.js:** Node.js 기반, 경량화된 웹 프레임워크, 빠른 개발 속도

### 빈의 생명주기와 콜백

**빈 생명주기 콜백:**
- Spring에서는 빈의 생명주기를 관리하기 위해 다양한 콜백 메서드를 제공합니다.
- `InitializingBean` 인터페이스의 `afterPropertiesSet` 메서드와 `DisposableBean` 인터페이스의 `destroy` 메서드를 사용할 수 있습니다.

### 빈 스코프와 프록시 모드

**주요 스코프 종류:**
- **싱글톤(Singleton):** 기본 스코프, 애플리케이션 전체에서 하나의 인스턴스만 생성
- **프로토타입(Prototype):** 빈 요청 시마다 새로운 인스턴스 생성
- **리퀘스트(Request):** HTTP 요청마다 새로운 인스턴스 생성
- **세션(Session):** HTTP 세션마다 새로운 인스턴스 생성
- **애플리케이션(Application):** 서블릿 컨텍스트마다 새로운 인스턴스 생성

**프록시 모드:**
- 웹 애플리케이션 단위의 스코프에서 프록시 모드를 사용하여 지연 로딩을 구현할 수 있습니다.

### 자바에서 SQL 직접 다루기와 JPA

**JDBC 사용:**
- 자바에서 SQL을 직접 다루기 위해 JDBC를 사용할 수 있습니다.
- 반복적인 코드와 SQL 의존성 문제가 발생할 수 있습니다.

**JPA 사용 이유:**
- JPA는 객체와 데이터베이스 간의 패러다임 불일치를 해결합니다.
- 엔티티 매핑을 통해 객체지향적으로 데이터를 관리할 수 있습니다.

**JPA의 쿼리 생성 과정:**
- JPA는 엔티티 매핑을 기반으로 자동으로 SQL 쿼리를 생성합니다.

### 결론

Spring과 Spring Boot는 객체지향 프로그래밍과 느슨한 결합을 통해 유연하고 확장 가능한 애플리케이션을 개발할 수 있도록 도와줍니다. 다양한 스코프와 의존성 주입을 통해 효과적으로 빈을 관리하고, JPA를 통해 데이터베이스와의 상호작용을 간편하게 할 수 있습니다. 이러한 장점을 활용하여 효율적인 개발을 할 수 있습니다.