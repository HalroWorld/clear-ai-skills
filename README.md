# clear-ai-skills

AI에게는 정확한 요청을, 사람에게는 이해하기 쉬운 답변을 만들어 주는 스킬 모음입니다.

## 스킬

### `intent-clarifier`

자연스럽고 모호한 말을 AI가 실행하기 좋은 요청으로 정리합니다.

- 목적·조건·결과물을 구분합니다.
- “옆에서 나오는 메뉴”처럼 말한 UI를 “드로어”처럼 정확한 이름으로 연결합니다.
- “폰에서 화면이 옆으로 밀려요” 같은 CSS 증상을 관찰한 문제와 원하는 결과 중심으로 정리합니다.
- 정리한 내용이 맞는지 먼저 묻고, 사용자가 동의한 뒤에만 최종 요청으로 확정합니다.

### `simple-explanation`

답변의 난이도를 먼저 판단하고, 기술적이거나 낯선 내용은 사용자가 요청하기 전부터 쉬운 한국어로 설명합니다.

- “쉽게 설명해줘”라는 요청이 없어도 필요한 경우 자동으로 적용합니다.
- 결론을 먼저 말합니다.
- UI 용어를 “드로어 → 화면 옆에서 나오는 메뉴”처럼 풀이합니다.
- CSS 용어를 “padding → 상자 안쪽 여백”처럼 풀이합니다.
- 완료·예정·미확인 상태와 중요한 조건을 그대로 유지합니다.

두 스킬에는 UI 요소 36개와 CSS 증상 42개를 담은 사전이 함께 들어 있습니다.

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

요청이 스킬 설명에 맞으면 Claude가 자동으로 사용할 수도 있습니다. 플러그인 업데이트는 `/plugin marketplace update clear-ai-skills`로 확인할 수 있으며, 마켓플레이스의 자동 업데이트를 켜면 시작할 때 새 버전을 받습니다.

직접 설치하려면 `plugins/clear-ai-skills/skills/` 아래의 원하는 스킬 폴더를 `~/.claude/skills/`로 복사하세요. 자세한 규칙은 [Claude Code 공식 플러그인 문서](https://code.claude.com/docs/en/plugins)를 참고하세요.

## 출처

UI·CSS 사전의 일부는 [Giting UI 메뉴판](https://giting.kr/skills/ui-menu)과 [CSS 증상 사전](https://giting.kr/skills/css-menu)을 바탕으로 작성했습니다. 원본 저작권과 MIT 라이선스 고지는 각 스킬의 `references/`에 포함되어 있습니다.
