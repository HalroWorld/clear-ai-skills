# clear-ai-skills

AI에게는 정확한 요청을, 사람에게는 이해하기 쉬운 답변을 만들어 주는 스킬 모음입니다.

## 스킬

### `intent-clarifier`

자연스럽고 모호한 말을 AI가 실행하기 좋은 요청으로 정리합니다.

- 목적·조건·결과물을 구분합니다.
- “옆에서 나오는 메뉴”처럼 말한 UI를 “드로어”처럼 정확한 이름으로 연결합니다.
- “폰에서 화면이 옆으로 밀려요” 같은 CSS 증상을 관찰한 문제와 원하는 결과 중심으로 정리합니다.
- 서버·네트워크·프론트엔드·백엔드·언어 관련 증상도 정리하며, 확인하지 않은 원인이나 해결책은 덧붙이지 않습니다.
- “좋겠어”, “했으면 해”, “원해”, “달라고”처럼 원하는 결과나 결과물을 말하면 모호하지 않은지 판단해 자동으로 요청을 정리합니다.
- 확인이 필요한 사항에는 `1.`, `2.`, `3.`처럼 번호를 매깁니다. 선택지로 나뉘면 선택지를 제시하고, 근거가 있는 추천 항목에는 `(추천)`과 이유를 표시합니다.
- 정리한 내용이 맞는지 먼저 묻고, 사용자가 동의한 뒤에만 최종 요청으로 확정합니다.

### `simple-explanation`

답변의 난이도를 먼저 판단하고, 기술적이거나 낯선 내용은 사용자가 요청하기 전부터 쉬운 한국어로 설명합니다.

- “쉽게 설명해줘”라는 요청이 없어도 필요한 경우 자동으로 적용합니다.
- 결론을 먼저 말합니다.
- UI 용어를 “드로어 → 화면 옆에서 나오는 메뉴”처럼 풀이합니다.
- CSS 용어를 “padding → 상자 안쪽 여백”처럼 풀이합니다.
- 개발 용어도 “타임아웃 → 정해진 시간 안에 끝나지 않아 기다리기를 중단한 상태”처럼 풀이합니다.
- 완료·예정·미확인 상태와 중요한 조건을 그대로 유지합니다.

두 스킬에는 UI 요소 36개, CSS 증상 42개와 개발 용어 34개를 담은 사전이 함께 들어 있습니다. 사전은 관련 질문이나 답변에 필요한 부분만 읽도록 연결되어 있습니다.

### 개발 영역 예시

[개발 사전](shared/development-dictionary.md)은 다음 다섯 영역마다 요청 정리 예시와 쉬운 답변 예시를 제공합니다.

| 영역 | 사용자가 한 말 | `intent-clarifier`가 정리하는 요청 | `simple-explanation`이 쉽게 풀이하는 말 |
| --- | --- | --- | --- |
| 서버·운영 | “로컬에서는 되는데 배포하면 꺼져” | 배포 환경에서 앱이 종료되는 원인을 조사하고 실행되도록 수정 | 환경 변수 → 실행에 필요한 설정값 |
| 네트워크 | “집에서는 접속되는데 회사에서는 안 돼” | 회사 네트워크에서 접속되지 않는 원인을 조사하고 해결 | 타임아웃 → 제한 시간 안에 끝나지 않아 기다리기를 중단한 상태 |
| 프론트엔드 | “새로고침해도 작성 중인 글이 남았으면 해” | 새로고침 후에도 작성 중인 글이 유지되도록 수정 | 상태 → 화면 동작이나 표시를 결정하는 현재 데이터 |
| 백엔드·데이터 | “저장을 두 번 누르면 같은 글이 두 개 생겨” | 연속 저장으로 글이 중복 생성되는 원인을 조사하고 중복되지 않도록 수정 | 인가 → 로그인은 됐지만 해당 작업 권한이 있는지 판단하는 과정 |
| 프로그래밍 언어·실행 환경 | “입력창 값을 쓰려는데 숫자 타입이 필요하대” | 입력값과 숫자 타입의 불일치를 조사하고 올바르게 처리 | 예외 → 실행 중 발생한 오류를 전달하는 방식 |

JavaScript, TypeScript, Python, Java, Go, Rust 관련 기초 용어를 포함합니다. 증상에 이름을 붙이는 것과 실제 원인을 진단하는 것은 구분합니다.

## Codex 플러그인 설치

마켓플레이스를 등록하고 플러그인을 설치합니다.

```bash
codex plugin marketplace add HalroWorld/clear-ai-skills
codex plugin add clear-ai-skills@clear-ai-skills
```

새 대화에서 다음처럼 사용할 수 있습니다.

```text
$clear-ai-skills:intent-clarifier 이 요청을 AI가 이해하기 쉽게 정리해줘.
$clear-ai-skills:simple-explanation 아래 답변을 쉽게 설명해줘.
```

직접 설치하려면 `plugins/clear-ai-skills/skills/` 아래의 원하는 스킬 폴더를 `~/.codex/skills/`로 복사하세요.

## Claude Code 플러그인 설치

Claude Code에서 마켓플레이스를 등록하고 플러그인을 설치합니다.

```text
/plugin marketplace add HalroWorld/clear-ai-skills
/plugin install clear-ai-skills@clear-ai-skills
```

설치 후 다음처럼 호출합니다.

```text
/clear-ai-skills:intent-clarifier 이 요청을 AI가 이해하기 쉽게 정리해줘.
/clear-ai-skills:simple-explanation 아래 답변을 쉽게 설명해줘.
```

요청이 스킬 설명에 맞으면 Claude가 자동으로 사용할 수도 있습니다.

### 최신 버전 유지하기

서드파티 마켓플레이스는 자동 업데이트가 **기본으로 꺼져 있습니다.** 한 번만 켜두면 이후로는 알아서 최신 버전을 받습니다.

1. `/plugin` 실행
2. **Marketplaces** 탭에서 `clear-ai-skills` 선택
3. **Enable auto-update** 선택

세션을 시작하고 잠시 뒤 백그라운드로 갱신되며, 새 버전을 받으면 `/reload-plugins` 안내가 뜹니다. 지금 바로 받고 싶다면:

```text
/plugin marketplace update clear-ai-skills
/plugin update clear-ai-skills
```

플러그인 대신 스킬 폴더를 `~/.claude/skills/`로 직접 복사할 수도 있지만 권장하지 않습니다. 복사본은 업데이트되지 않고, 이름이 같은 플러그인 스킬을 가려서 `/intent-clarifier`가 계속 옛 버전으로 실행됩니다. 자세한 규칙은 [Claude Code 공식 플러그인 문서](https://code.claude.com/docs/en/plugins)를 참고하세요.

## 라이선스

이 프로젝트는 [MIT License](LICENSE)로 배포됩니다.

## 출처

UI·CSS 사전의 일부는 [Giting UI 메뉴판](https://giting.kr/skills/ui-menu)과 [CSS 증상 사전](https://giting.kr/skills/css-menu)을 바탕으로 작성했습니다. 원본 저작권과 MIT 라이선스 고지는 각 스킬의 `references/`에 포함되어 있습니다.
