#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
# class Solution:
#     def carFleet(self, target: int, position: [int], speed: [int]) -> int:
#         stack = []
#         cars=[] # position : speed
#         for i in range(len(position)):
#             cars.append({
#                 'position': position[i],
#                 'speed': speed[i]
#             })
#         cars.sort(key=lambda x: x['position'], reverse=True)
#         print(cars)
#         def collides(b, f, target) ->bool:
#             if b['speed'] <= f['speed']:
#                 return False
#             # 前の車両がゴールする時間に、後ろの車両がゴールを超えているかを判定する
#             t = (target - f['position']) / f['speed']
#             return b['position'] + b['speed'] * t >= target
#         for car in cars:
#             if not stack:
#                 stack.append(car)
#                 continue
#             if collides(car, stack[-1], target):
#                 continue
#             else:
#                 stack.append(car)
#         return len(stack)
    
class Solution:
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


# @lc code=end

input = {
    'self': None,
    'target': 10,
    'position': [6,8],
    'speed': [3,2],
}
Solution.carFleet(**input)

#動画の説明を聞いてから、自力で解けた！嬉しい。
# コードの長さやメモリが課題