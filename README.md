# clear-ai-skills

막연한 질문은 정확한 요청으로, 복잡한 AI 답변은 쉬운 설명으로 바꿔주는 스킬 모음입니다.

AI와 대화할 때 자주 필요한 두 가지 작업을 위한 스킬 모음입니다.

## 포함된 스킬

### `simple-explanation` — 쉽게 설명하기

전문적이고 복잡한 AI 답변을 핵심 중심의 쉬운 말로 풀어줍니다. 기술 용어는 필요한 만큼 유지하고, 중요한 조건과 아직 확인하지 않은 내용은 빠뜨리지 않습니다.

UI 사전을 활용해 “드로어 메뉴를 추가했습니다”를 “화면 옆에서 나오는 메뉴를 추가했습니다”처럼 전달합니다.

CSS 설명도 “padding을 조정했습니다”를 “상자 안쪽 여백을 조정했습니다”처럼 풀어 씁니다. 원문의 추측과 확인 여부는 유지합니다.

### `intent-clarifier` — 요청을 정확하게 다시 정리하기

사용자가 자연스럽게 작성한 질문을 AI가 실행하기 좋은 간결한 요청으로 정리합니다. 목적, 조건, 결과물을 구분하고 모호한 부분은 추측하지 않습니다.

UI 사전을 활용해 “옆에서 나오는 메뉴”를 “드로어”처럼 정확한 이름으로 연결합니다. “팝업”처럼 뜻이 여러 개면 필요한 동작을 확인합니다.

정리한 의도를 곧바로 확정하지 않고, “제가 이해한 요청이 맞나요?”라고 사용자에게 먼저 확인합니다.

“폰에서 화면이 옆으로 밀려요” 같은 CSS 증상은 관찰한 문제와 원하는 결과 중심으로 정리합니다. 확인하지 않은 원인이나 처방은 단정하지 않습니다.

## 공통 UI 사전

두 스킬은 [같은 사전](shared/ui-dictionary.md)을 서로 반대 방향으로 활용합니다. 현재 자주 쓰는 UI 요소 36개에 정식 명칭, 일상 표현, 쉬운 설명과 필요한 구분 기준을 담았습니다. UI 관련 요청이나 답변에서만 필요한 항목을 읽습니다.

[Giting UI 메뉴판](https://giting.kr/skills/ui-menu)의 사전 데이터를 발췌·수정했습니다. 원본의 저작권과 [MIT 라이선스 전문](shared/LICENSE-ui-menu.txt)을 함께 보존합니다. 이 고지는 가져온 자료에 적용됩니다.

## 공통 CSS 사전

[CSS 사전](shared/css-dictionary.md)은 정렬·넘침·스크롤·겹침·모바일·간격·글자·표시 문제 42개와 CSS 용어 풀이를 담습니다. `intent-clarifier`는 증상을 요청으로, `simple-explanation`은 AI의 CSS 설명을 일상 언어로 바꿀 때 활용합니다.

[Giting CSS 증상 사전](https://giting.kr/skills/css-menu)에서 증상과 원인 후보 등을 발췌하고 [MIT 고지](shared/LICENSE-css-menu.txt)를 보존했습니다. 원인 후보는 진단 결과가 아니며, 실제 수정과 검증을 대신하지 않습니다.

## 사전 개선하기

`shared/ui-dictionary.md` 또는 `shared/css-dictionary.md`를 수정한 뒤 아래 명령으로 두 스킬에 반영하세요. 기존 이름의 스크립트가 UI·CSS 사전과 고지를 모두 동기화합니다. 각 스킬 폴더에 실제 사본이 들어 있어 하나만 설치해도 사용할 수 있습니다.

```bash
python3 scripts/sync-ui-dictionary.py
python3 scripts/sync-ui-dictionary.py --check
```

## 설치

Codex에서는 원하는 스킬 폴더 전체(`SKILL.md`, `agents/`, `references/` 포함)를 개인 스킬 디렉터리에 복사합니다.

```text
clear-ai-skills/
└─ agent-skills/
   ├─ simple-explanation/
   └─ intent-clarifier/
```

기본 설치 위치는 다음과 같습니다.

```text
~/.codex/skills/simple-explanation/
~/.codex/skills/intent-clarifier/
```

새 대화에서 호출할 수 있습니다.

```text
$simple-explanation 이 답변을 쉽게 설명해줘.
$intent-clarifier 이 요청을 AI가 이해하기 쉽게 정리해줘.
```

다른 AI 도구에서는 각 스킬의 `SKILL.md` 내용을 시스템 지침이나 사용자 지침으로 제공하면 됩니다. UI 용어에는 `references/ui-dictionary.md`, CSS 증상이나 용어에는 `references/css-dictionary.md`를 함께 제공하세요. 설치 방식과 스킬 자동 호출 지원 여부는 도구마다 다릅니다.

## 목표

전문 용어나 긴 설명을 몰라도 누구나 AI를 편하게 사용하도록 돕습니다. 답변을 무조건 줄이는 것이 아니라, 핵심·조건·다음 행동을 이해하기 쉬운 형태로 전달하는 것을 목표로 합니다.

## 상태

현재는 초기 버전입니다. 사용하면서 이해하기 어려웠던 답변이나 개선 의견을 기록해 주세요.
