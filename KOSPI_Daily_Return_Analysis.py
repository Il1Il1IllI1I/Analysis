import pandas as pd

# CSV 파일 읽기
file_path = 'KOSPI_1_years_daily_return_code.csv'
df = pd.read_csv(file_path)

# 데이터 프레임의 처음 몇 행을 보여줌
df.head()

from typing import List, Tuple

def find_declining_companies(df: pd.DataFrame, N: int) -> Tuple[List[str], List[float]]:
    """
    N일 연속으로 일별 수익률이 0과 같거나 작았던 기업을 찾고,
    이 기업들을 N일간의 하락폭이 큰 순서로 정렬한다.
    
    Parameters:
    - df: 일별 수익률이 있는 데이터프레임
    - N: 연속 하락일 수 (최소 3)
    
    Returns:
    - declining_companies: N일 연속으로 하락한 기업 리스트
    - declines: 각 기업의 N일간 누적 하락률
    """
    if N < 3:
        raise ValueError("N은 최소 3 이상이어야 합니다.")
        
    # Date 컬럼을 제외한 모든 기업(컬럼)에 대해 연산
    companies = df.columns[1:]
    declining_companies = []
    declines = []
    
    for company in companies:
        # 해당 기업의 일별 수익률을 가져옴
        daily_returns = df[company].dropna()
        
        # N일 연속 하락했는지 검사
        for i in range(len(daily_returns) - N):
            if all(daily_returns.iloc[i:i+N] <= 0):
                # N일 동안의 누적 수익률 계산
                cumulative_return = (daily_returns.iloc[i:i+N] / 100 + 1).prod() - 1
                
                declining_companies.append(company)
                declines.append(cumulative_return * 100)
                break  # 이미 N일 연속 하락을 확인했으므로 다음 기업으로 넘어감
    
    # N일간의 하락폭이 큰 순서로 정렬
    sorted_indices = sorted(range(len(declines)), key=lambda k: declines[k])
    declining_companies = [declining_companies[i] for i in sorted_indices]
    declines = [declines[i] for i in sorted_indices]
    
    return declining_companies, declines

# 테스트: N을 3으로 설정
N = 3
declining_companies, declines = find_declining_companies(df, N)
declining_companies[:10], declines[:10]  # 상위 10개만 출력

def calculate_next_day_performance(df: pd.DataFrame, declining_companies: List[str], N: int) -> Tuple[int, int, float]:
    """
    N일 연속 하락한 기업 중, 다음날 수익률이 어떤지 분석한다.
    
    Parameters:
    - df: 일별 수익률이 있는 데이터프레임
    - declining_companies: N일 연속으로 하락한 기업 리스트
    - N: 연속 하락일 수 (최소 3)
    
    Returns:
    - num_positive: 다음날 수익률이 양수인 기업의 수
    - num_negative: 다음날 수익률이 음수인 기업의 수
    - ratio: 다음날 수익률이 양수인 기업의 비율
    """
    num_positive = 0  # 다음날 수익률이 양수인 기업의 수
    num_negative = 0  # 다음날 수익률이 음수인 기업의 수
    
    for company in declining_companies:
        # 해당 기업의 일별 수익률을 가져옴
        daily_returns = df[company].dropna()
        
        # N일 연속 하락했는지 검사
        for i in range(len(daily_returns) - N):
            if all(daily_returns.iloc[i:i+N] <= 0):
                next_day_return = daily_returns.iloc[i+N]  # N일 동안 하락한 후 바로 다음 거래일의 수익률
                
                if next_day_return > 0:
                    num_positive += 1
                else:
                    num_negative += 1
                
                break  # 이미 N일 연속 하락을 확인했으므로 다음 기업으로 넘어감
    
    # 다음날 수익률이 양수인 기업의 비율
    ratio = num_positive / len(declining_companies) if declining_companies else 0
    
    return num_positive, num_negative, ratio

# N일 연속 하락한 기업 중, 다음날의 수익률 분석
num_positive, num_negative, ratio = calculate_next_day_performance(df, declining_companies, N)
num_positive, num_negative, ratio

def calculate_average_next_day_return(df: pd.DataFrame, declining_companies: List[str], N: int) -> float:
    """
    N일 연속 하락한 기업 중, 다음날의 평균 수익률을 계산한다.
    
    Parameters:
    - df: 일별 수익률이 있는 데이터프레임
    - declining_companies: N일 연속으로 하락한 기업 리스트
    - N: 연속 하락일 수 (최소 3)
    
    Returns:
    - average_next_day_return: 다음날의 평균 수익률
    """
    next_day_returns = []  # 다음날 수익률 리스트
    
    for company in declining_companies:
        # 해당 기업의 일별 수익률을 가져옴
        daily_returns = df[company].dropna()
        
        # N일 연속 하락했는지 검사
        for i in range(len(daily_returns) - N):
            if all(daily_returns.iloc[i:i+N] <= 0):
                next_day_return = daily_returns.iloc[i+N]  # N일 동안 하락한 후 바로 다음 거래일의 수익률
                next_day_returns.append(next_day_return)
                break  # 이미 N일 연속 하락을 확인했으므로 다음 기업으로 넘어감
    
    # 다음날의 평균 수익률 계산
    average_next_day_return = sum(next_day_returns) / len(next_day_returns) if next_day_returns else 0
    
    return average_next_day_return

# 1번 조건을 만족하는 모든 기업의 다음날 평균 수익률 계산
average_next_day_return = calculate_average_next_day_return(df, declining_companies, N)
average_next_day_return

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# 한글 폰트 설정 (Mac용)
# plt.rcParams['font.family'] = 'AppleGothic'
# Windows용
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')  # ggplot 스타일 사용

def visualize_top_companies(declining_companies: List[str], declines: List[float], N: int):
    """
    N일 연속 하락한 기업 중, 다음날 수익률이 가장 높은 상위 10개 기업을 시각화한다.
    
    Parameters:
    - declining_companies: N일 연속으로 하락한 기업 리스트
    - declines: 각 기업의 N일간 누적 하락률
    - N: 연속 하락일 수 (최소 3)
    """
    # 상위 10개 기업만 선택 (다음날 수익률이 가장 높은 기업)
    top_10_companies = declining_companies[:10]
    top_10_declines = declines[:10]
    
    # 시각화
    plt.figure(figsize=(15, 8))
    plt.barh(top_10_companies, top_10_declines, color='red')
    plt.xlabel(f'{N}일간 누적 하락률 (%)')
    plt.title(f'{N}일 연속 하락한 후 다음날 수익률이 가장 높은 상위 10개 기업')
    for i, v in enumerate(top_10_declines):
        plt.text(v, i, f"{v:.2f}%", color='blue', va='center', ha='left')
    plt.show()

# 상승폭이 큰 순서로 정렬된 기업들을 시각화
visualize_top_companies(declining_companies, declines, N)
