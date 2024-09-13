 # main.py

 def calculate_process_time(box_counts, process_times):
     """
     각 공정에 대해 박스 수량을 기반으로 처리 시간을 계산합니다.
     
     :param box_counts: 각 공정에서 처리할 박스의 수량 리스트
     :param process_times: 각 공정에서 박스 하나를 처리하는 데 걸리는 시간 리스트 (초 단위)
     :return: 각 공정의 소요 시간과 전체 소요 시간
     """
     total_time = 0
     process_durations = []

     for i in range(len(box_counts)):
         process_duration = box_counts[i] * process_times[i]
         process_durations.append(process_duration)
         total_time += process_duration
         print(f"공정 {i+1}의 소요 시간: {process_duration}초")

     print(f"전체 공정 완료 시간: {total_time}초")
     return process_durations, total_time

 # 예시 데이터
 box_counts = [10, 5, 8]  # 각 공정에서 처리할 박스 수량
 process_times = [2, 3, 1]  # 각 공정에서 박스 하나를 처리하는 데 걸리는 시간 (초 단위)

 # 시뮬레이션 실행
 calculate_process_time(box_counts, process_times)
 ```
