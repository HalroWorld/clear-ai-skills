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

AI의 기술적인 답변을 핵심 중심의 쉬운 한국어로 바꿉니다.

- 결론을 먼저 말합니다.
- UI 용어를 “드로어 → 화면 옆에서 나오는 메뉴”처럼 풀이합니다.
- CSS 용어를 “padding → 상자 안쪽 여백”처럼 풀이합니다.
- 완료·예정·미확인 상태와 중요한 조건을 그대로 유지합니다.

두 스킬에는 UI 요소 36개와 CSS 증상 42개를 담은 사전이 함께 들어 있습니다.

## Codex에서 사용하기

원하는 스킬 폴더를 전역 스킬 디렉터리에 복사합니다.

```bash
cp -R agent-skills/intent-clarifier ~/.codex/skills/
cp -R agent-skills/simple-explanation ~/.codex/skills/
```

새 대화에서 다음처럼 사용할 수 있습니다.

```text
$intent-clarifier 이 요청을 AI가 이해하기 쉽게 정리해줘.
$simple-explanation 아래 답변을 쉽게 설명해줘.
```

전역 설치를 원하지 않으면 각 스킬 폴더의 `SKILL.md`를 다른 AI 도구의 지침으로 제공하세요. UI·CSS 용어를 다룰 때는 같은 폴더의 `references/` 파일도 함께 제공해야 합니다.

## 출처

UI·CSS 사전의 일부는 [Giting UI 메뉴판](https://giting.kr/skills/ui-menu)과 [CSS 증상 사전](https://giting.kr/skills/css-menu)을 바탕으로 작성했습니다. 원본 저작권과 MIT 라이선스 고지는 각 스킬의 `references/`에 포함되어 있습니다.
