# 개발 용어·증상 사전

일상적인 표현을 개발 요청으로 정리하거나 기술 답변을 쉽게 작성할 때 사용하는 참고 자료다. 증상은 원인을 증명하지 않는다. 아래 확인 지점은 진단 결과나 반드시 적용할 해결책이 아니다.

각 항목은 한국어와 영어 표현을 함께 담는다. `쉬운 뜻`과 `Plain meaning`은 같은 내용의 두 언어 판이고, 일상 표현 칸에는 두 언어의 표현을 나란히 적었다. 사용자가 쓴 언어의 표현으로 항목을 찾고 설명도 같은 언어로 돌려준다. 확인 지점은 언어와 무관한 판단 기준이므로 한국어로만 적고, 답변할 때 사용자의 언어로 옮긴다.

## 필요한 부분 찾기

| 영역 | 검색어 | Search terms |
| --- | --- | --- |
| 서버·운영 | 서버, 프로세스, 배포, 환경 변수, 로그, 메모리 | server, process, deploy, environment variable, log, memory |
| 네트워크 | DNS, 포트, HTTP, TLS, 타임아웃, 연결 | DNS, port, HTTP, TLS, timeout, connection |
| 프론트엔드 | 렌더링, 상태, 이벤트, 라우팅, 캐시 | rendering, state, event, routing, cache |
| 백엔드·데이터 | API, 인증, 인가, 데이터베이스, 트랜잭션 | API, authentication, authorization, database, transaction |
| 언어·실행 환경 | JavaScript, TypeScript, Python, Java, Go, Rust, 예외, 비동기 | JavaScript, TypeScript, Python, Java, Go, Rust, exception, async |

현재 질문에 해당하는 영역과 항목만 읽는다. 여러 영역에 걸치면 관련 항목을 함께 확인하되, 한 영역의 원인으로 미리 확정하지 않는다. 예시는 사용자가 실제로 제공한 조건에 맞게 사용한다.

## 서버·운영

| 용어 | 쉬운 뜻 | Plain meaning | 일상 표현·확인 지점 |
| --- | --- | --- | --- |
| 서버 | 다른 프로그램의 요청을 받아 처리하는 프로그램이나 컴퓨터 | A program or machine that receives and handles requests from other programs | “서버가 죽었어” / "the server is down": 접속 불가인지, 프로그램 종료인지, 특정 기능 실패인지 구분 |
| 프로세스 | 실행 중인 프로그램 | A program that is currently running | “켜자마자 꺼져” / "it dies the moment I start it": 종료 시점과 오류 기록 확인, 메모리 부족으로 단정하지 않기 |
| 배포 | 수정한 프로그램을 사용 환경에 반영하는 작업 | The work of putting modified code into the environment where it is used | “내 컴퓨터에서는 되는데 올리면 안 돼” / "works on my machine but not once it's deployed": 환경과 실패하는 작업 구분 |
| 환경 변수 | 실행 환경에서 프로그램에 전달하는 설정값 | A configuration value passed to a program by the environment it runs in | “서버에서만 설정을 못 읽어” / "only the server can't read the settings": 변수 이름과 설정 위치 확인, 비밀값을 요구하지 않기 |
| 로그 | 프로그램이 남긴 동작·오류 기록 | The record a program leaves of what it did and what went wrong | “왜 실패했는지 모르겠어” / "I can't tell why it failed": 관련 시점의 기록 확인, 토큰·개인정보 가리기 |
| 메모리 부족 | 프로그램이 필요한 메모리를 확보하지 못하는 상태 | The state of a program failing to obtain the memory it needs | “오래 켜면 꺼져” / "it dies if I leave it running a long time": 사용량·종료 기록 없이 메모리 누수로 확정하지 않기 |

요청 정리 예: “배포하면 앱이 바로 꺼져. 로컬에서는 돼” → “로컬에서는 실행되지만 배포 환경에서 앱이 즉시 종료되는 원인을 조사하고, 배포 환경에서도 실행되도록 수정해 주세요.”

쉬운 답변 예: “환경 변수 누락이 원인으로 의심됩니다. 아직 미확인입니다” → “실행에 필요한 설정값이 빠졌을 가능성이 있습니다. 실제 원인인지는 아직 확인하지 않았습니다.”

## 네트워크

| 용어 | 쉬운 뜻 | Plain meaning | 일상 표현·확인 지점 |
| --- | --- | --- | --- |
| DNS | 도메인 이름에 해당하는 주소 등의 정보를 찾는 체계 | The system that looks up the address and related information for a domain name | “주소로 접속이 안 돼” / "I can't reach it by its address": 이름 조회 실패인지 연결 실패인지 구분 |
| 포트 | 한 컴퓨터에서 통신할 프로그램을 구분하는 번호 | A number distinguishing which program on a machine a connection is for | “연결이 거부돼” / "the connection is refused": 대상 주소·포트와 서비스 실행 상태 확인, 방화벽으로 단정하지 않기 |
| HTTP 요청·응답 | 웹에서 자료나 처리를 요청하고 결과를 돌려받는 메시지 | The messages that ask the web for data or an action and carry the result back | “버튼 눌러도 안 돼” / "nothing happens when I press the button": 요청 전송 여부와 응답 결과 구분 |
| TLS | 통신 내용을 암호화하고 상대의 신원을 확인하는 데 쓰는 기술 | The technology used to encrypt traffic and verify who the other side is | “인증서 경고가 떠” / "I get a certificate warning": 경고 문구·도메인 확인, 검증 해제를 해결책으로 넣지 않기 |
| 타임아웃 | 정해진 시간 안에 작업이 끝나지 않아 기다리기를 중단한 상태 | The state where work did not finish in the allotted time and the wait was abandoned | “계속 기다리다 실패해” / "it waits and waits, then fails": 어느 단계에서 시간이 초과됐는지 확인 |
| 프록시 | 요청과 응답을 중간에서 전달하는 서버 | A server that relays requests and responses in the middle | “중간 서버에서 에러가 나” / "the middle server throws an error": 실제 오류를 만든 지점과 전달한 지점 구분 |

요청 정리 예: “회사에서는 접속이 안 되고 집에서는 돼” → “집에서는 접속되지만 회사 네트워크에서는 접속되지 않는 원인을 조사하고 해결해 주세요.” 회사 보안 정책 변경을 미리 요구하지 않는다.

쉬운 답변 예: “요청이 타임아웃됐습니다” → “정해진 시간 안에 응답을 받지 못해 기다리기를 중단했습니다. 이것만으로 서버가 꺼졌다고 판단할 수는 없습니다.”

HTTP 요청·응답과 프록시의 기본 개념은 [MDN HTTP 개요](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)를 참고한다.

## 프론트엔드

| 용어 | 쉬운 뜻 | Plain meaning | 일상 표현·확인 지점 |
| --- | --- | --- | --- |
| 프론트엔드 | 사용자가 화면에서 보고 조작하는 부분 | The part the user sees and operates on screen | “화면이 안 떠” / "the page won't come up": 화면 코드·데이터 응답·연결 문제를 미리 구분하지 않기 |
| 렌더링 | 데이터와 화면 구조를 바탕으로 표시할 내용을 만드는 과정 | The process of producing what to display from data and screen structure | “값은 바뀌었는데 화면은 그대로야” / "the value changed but the screen didn't": 실제 데이터와 표시 결과 구분 |
| 상태(state) | 화면 동작이나 표시를 결정하는 현재 데이터 | The current data that decides how the screen behaves and what it shows | “새로고침하면 입력이 사라져” / "my input disappears when I refresh": 유지할 데이터와 유지 기간 확인 |
| 이벤트 처리 | 클릭·입력 같은 동작에 반응해 실행하는 코드 | Code that runs in response to an action such as a click or keystroke | “버튼이 먹통이야” / "the button is dead": 클릭 감지와 후속 작업 실패 구분 |
| 라우팅 | 주소에 따라 보여줄 화면을 선택하는 처리 | The handling that picks which screen to show based on the address | “링크로 바로 들어가면 안 돼” / "going straight to the link doesn't work": 앱 안에서 이동할 때와 직접 접속할 때 비교 |
| 캐시 | 다시 사용하려고 저장해 둔 데이터 | Data stored so it can be reused | “수정했는데 옛날 내용이 보여” / "I changed it but I still see the old content": 어느 데이터가 오래됐는지 확인, 캐시 삭제를 미리 처방하지 않기 |

요청 정리 예: “새로고침하면 작성하던 글이 없어져. 남아 있었으면 해” → “새로고침 후에도 작성 중인 글이 유지되도록 수정해 주세요.” 저장 위치·기간·공유 범위가 필요하면 확인한다.

쉬운 답변 예: “상태는 갱신됐지만 화면 렌더링에는 반영되지 않았습니다” → “프로그램 안의 값은 바뀌었지만, 화면에는 바뀐 값이 아직 표시되지 않았습니다.”

## 백엔드·데이터

| 용어 | 쉬운 뜻 | Plain meaning | 일상 표현·확인 지점 |
| --- | --- | --- | --- |
| 백엔드 | 화면 뒤에서 요청 처리와 데이터 관리를 담당하는 부분 | The part behind the screen handling requests and managing data | “저장 버튼을 눌러도 저장 안 돼” / "pressing save doesn't save": 화면·통신·저장 처리 중 어디서 실패했는지 미확정 |
| API | 프로그램끼리 기능이나 데이터를 주고받는 약속과 접점 | The agreed interface through which programs exchange functionality or data | “다른 서비스랑 연결하고 싶어” / "I want to connect it to another service": 주고받을 데이터와 작업 조건 확인 |
| 인증 | 누가 요청했는지 확인하는 과정 | The process of confirming who made a request | “로그인이 자꾸 풀려” / "it keeps logging me out": 발생 시점과 환경 확인, 만료 시간이 원인이라고 단정하지 않기 |
| 인가 | 확인된 사용자에게 해당 작업 권한이 있는지 판단하는 과정 | The process of deciding whether a confirmed user may perform this action | “로그인했는데 못 들어가” / "I'm logged in but I still can't get in": 로그인 성공과 접근 권한은 별개 |
| 데이터베이스 쿼리 | 저장된 데이터를 조회하거나 변경하는 요청 | A request that reads or changes stored data | “검색이 느려” / "search is slow": 처리 시간 확인 전 쿼리나 인덱스 문제로 단정하지 않기 |
| 트랜잭션 | 여러 데이터 작업을 하나의 성공·실패 단위로 묶는 처리 | Handling that binds several data operations into a single success-or-failure unit | “일부만 저장돼” / "only part of it got saved": 함께 성공하거나 취소돼야 하는 작업 범위 확인 |
| 멱등성 | 같은 요청을 반복해도 의도한 효과가 한 번 수행한 것과 같도록 하는 성질 | The property that repeating the same request has the same intended effect as performing it once | “두 번 누르면 중복 저장돼” / "pressing twice saves it twice": 같은 요청의 식별 기준 확인, 버튼 비활성화만으로 해결됐다고 단정하지 않기 |

요청 정리 예: “저장을 두 번 누르면 같은 글이 두 개 생겨” → “저장 버튼을 연속으로 누를 때 같은 글이 중복 생성되는 원인을 조사하고, 중복 저장되지 않도록 수정해 주세요.”

쉬운 답변 예: “인증은 성공했지만 인가에 실패했습니다” → “로그인은 됐지만, 이 작업을 할 권한은 없는 상태입니다.”

## 프로그래밍 언어·실행 환경

언어와 프레임워크를 구분한다. JavaScript는 언어, Node.js는 JavaScript 실행 환경, React는 화면을 만드는 라이브러리다. 프론트엔드·백엔드는 담당 역할이며 언어 이름만으로 실행 위치를 확정하지 않는다.

| 용어 | 쉬운 뜻 | Plain meaning | 일상 표현·확인 지점 |
| --- | --- | --- | --- |
| JavaScript | 브라우저나 서버 실행 환경 등에서 사용하는 프로그래밍 언어 | A programming language used in browsers, server runtimes, and elsewhere | “자바스크립트가 안 돼” / "JavaScript isn't working": 브라우저인지 서버인지 확인 |
| TypeScript·타입 검사 | JavaScript에 값의 종류를 검사하는 기능 등을 더한 언어·검사 | A language and checker adding value-type checking and more on top of JavaScript | “문자를 넣었더니 타입 에러” / "I passed a string and got a type error": 기대한 값과 실제 값 구분, 검사를 끄도록 요구하지 않기 |
| Python·예외 | Python 실행 중 발생한 오류 등을 전달하는 방식 | The mechanism that reports errors raised while Python runs | “파이썬이 에러 뿜어” / "Python is spitting out an error": 예외 종류와 발생 위치 확인, 오류를 숨기는 처방 금지 |
| Java·JVM | Java는 언어, JVM은 Java 바이트코드 등을 실행하는 가상 머신 | Java is the language; the JVM is the virtual machine that runs Java bytecode and similar | “자바가 안 켜져” / "Java won't start": 설치·컴파일·실행 중 어느 단계인지 확인, JavaScript와 구분 |
| Go·goroutine | Go에서 다른 작업과 함께 진행하도록 실행하는 함수 작업 단위 | A unit of function work Go runs so it proceeds alongside other work | “고루틴 늘렸는데 안 빨라져” / "I added goroutines and it got no faster": 동시에 진행하는 것과 속도 개선을 동일시하지 않기 |
| Rust·소유권 | 값의 사용과 정리를 관리하는 Rust의 규칙 | Rust's rules governing how values are used and cleaned up | “값을 옮긴 뒤 못 쓴대” / "it says I can't use the value after moving it": 오류 문구와 사용 위치 확인, 무조건 복제하라고 요구하지 않기 |
| 컴파일·빌드 | 코드를 실행 가능한 형태로 바꾸거나 배포할 결과물을 만드는 작업 | Turning code into a runnable form, or producing the artefact to be deployed | “빌드가 깨져” / "the build is broken": 빌드 단계 실패와 실행 후 실패 구분 |
| 런타임 오류 | 프로그램 실행 중 발생하는 오류 | An error that occurs while the program is running | “검사는 통과했는데 켜면 실패해” / "it passes the checks but fails when I run it": 검사 통과가 모든 실행 상황의 성공을 보장하지 않음 |
| 비동기·await | 작업 완료를 다루면서 다른 작업도 진행할 수 있게 하는 방식·완료를 기다리는 표현 | A way of handling completion that lets other work proceed, and the expression that waits for completion | “결과가 오기 전에 다음 코드가 돌아” / "the next line runs before the result arrives": 필요한 실행 순서 확인, 자동 병렬 실행으로 풀이하지 않기 |

요청 정리 예: “타입스크립트에서 숫자 넣으라는데 나는 입력창 값을 쓰고 싶어” → “입력창 값과 코드가 요구하는 숫자 타입 사이의 불일치를 조사하고, 입력값을 올바르게 처리하도록 수정해 주세요.” 빈 입력·유효하지 않은 입력의 처리가 필요하면 확인한다.

쉬운 답변 예: “Python에서 예외가 처리되지 않아 실행이 중단됐습니다” → “실행 중 오류가 발생했고, 이를 처리하는 코드가 없어 프로그램이 중단됐습니다.”

타입 검사의 역할은 [TypeScript 입문](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html), 구문 오류와 실행 중 예외의 구분은 [Python 오류와 예외](https://docs.python.org/3/tutorial/errors.html)를 참고한다. 사전은 특정 언어 버전의 문법이나 제품별 설정 방법을 대신하지 않는다.
