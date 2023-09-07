# Analysis
version_1

---

# 📈 KOSPI 일일 수익률 분석 (`KOSPI_Daily_Return_Analysis`)

## 🌟 개요

`KOSPI_Daily_Return_Analysis` 스크립트는 한국 거래소(KOSPI)에 상장된 기업들의 일일 수익률을 분석합니다. 특히, 연속된 일자(`N`일) 동안 하락한 기업을 식별한 후, 그 다음 거래일의 성과를 평가합니다.

## ✨ 주요 기능

1. **하락한 기업 찾기**: `N`일 동안 일일 수익률이 0 또는 음수였던 기업을 식별합니다.
2. **다음날 성과 계산**: 이러한 하락한 기업의 다음날 수익률을 분석합니다.
3. **다음날 평균 수익률 계산**: 이러한 기업들의 다음날 평균 수익률을 계산합니다.
4. **상위 기업 시각화**: 하락 후 다음날 수익률이 가장 높은 상위 10개 기업을 보여줍니다.

## 🚀 사용 방법

1. CSV 형식의 데이터셋을 로드합니다.
2. 분석하려는 연속적인 하락일의 수 `N` 값을 설정합니다.
3. 스크립트를 실행합니다.

## 🛠️ 필요 라이브러리

- pandas
- matplotlib

## 📜 스크립트 구성

- `find_declining_companies(df, N)`: `N`일 동안 연속으로 하락한 기업을 찾아 리스트로 반환합니다.
- `calculate_next_day_performance(df, declining_companies, N)`: 하락한 기업 중 다음날 양수와 음수 수익률을 계산합니다.
- `calculate_average_next_day_return(df, declining_companies, N)`: 하락한 기업 중 다음날의 평균 수익률을 계산합니다.
- `visualize_top_companies(declining_companies, declines, N)`: 상위 10개 하락 기업을 시각화합니다.

---

이 정보를 사용하여 `README.md` 파일을 만들면 이 코드의 목적과 사용 방법을 명확하게 전달할 수 있습니다.
