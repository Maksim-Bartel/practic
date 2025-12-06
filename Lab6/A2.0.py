import xml.etree.ElementTree as ET


def load_users_data():
 try:
  users_tree = ET.parse('users.xml')
  users = []
  for user_elem in users_tree.getroot().findall('user'):
    user = {
      'user_id': int(user_elem.find('user_id').text),
      'name': user_elem.find('name').text,
      'age': int(user_elem.find('age').text),
      'weight': int(user_elem.find('weight').text),
      'fitness_level': user_elem.find('fitness_level').text,
      'workouts': []
    }
    users.append(user)
  return users
 except FileNotFoundError:
  print("Файл не найден")
 return []


def load_workouts_data():
  try:
      workouts_tree = ET.parse('workouts.xml')
      workouts = []
      for workout_elem in workouts_tree.getroot().findall('workout'):
        workout = {
              'workout_id': int(workout_elem.find('workout_id').text),
              'user_id': int(workout_elem.find('user_id').text),
              'date': workout_elem.find('date').text,
              'type': workout_elem.find('type').text,
              'duration': int(workout_elem.find('duration').text),
              'distance': float(workout_elem.find('distance').text),
              'calories': int(workout_elem.find('calories').text),
              'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
              'intensity': workout_elem.find('intensity').text
         }
        workouts.append(workout)
      return workouts
  except FileNotFoundError:
      print(" Файл  не найден!")
      return []


def get_stats(users, workouts):
    stats = {}
    stats['total_workouts'] = len(workouts)
    stats['total_users'] = len(users)
    stats['total_calories'] = sum(workout['calories'] for workout in workouts)
    minuts = sum(workout['duration'] for workout in workouts)
    stats['total_duration'] = int(minuts //60)
    dist = sum(workout['distance'] for workout in workouts)
    stats['total_distance'] = dist
    return stats



def analyze_user_activity(users, workouts):
    total_works = []


    for user in users:
        user_id = user['user_id']
        name = user['name']
        fitness_level = user['fitness_level']


        user_workouts = []
        for workout in workouts:
            if workout['user_id'] == user_id:
                user_workouts.append(workout)


        total_workouts = len(user_workouts)

        total_calories = 0
        total_min = 0
        for workout in user_workouts:
            total_calories += workout['calories']
            total_min += workout['duration']

        total_hours = total_min / 60


        total_works.append({
            'name': name,
            'level': fitness_level,
            'workouts': total_workouts,
            'calories': total_calories,
            'hours': total_hours
        })

     total_works.sort(key=lambda x: x['workouts'], reverse=True)
      
     print("=" * 50)
     print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
     print("=" * 50)

     top = total_works[:3]
     for i, user in enumerate(top, 1):
         print(f" {i}. {user['name']} ({user['level']}):")
         print(f"    Тренировок: {user['workouts']}")
         print(f"    Калорий: {user['calories']}")
         print(f"    Время: {user['hours']:.1f} часов")
         print()
      


def analyze_workout_types(workouts):



    print("\nРАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    print("-" * 40)

    type_stats = {}


    for workout in workouts:
        workout_type = workout['type']

        if workout_type not in type_stats:
            type_stats[workout_type] = {
                'count': 0,
                'total_duration': 0,
                'total_calories': 0
            }

        type_stats[workout_type]['count'] += 1
        type_stats[workout_type]['total_duration'] += workout['duration']
        type_stats[workout_type]['total_calories'] += workout['calories']

    total_workouts = len(workouts)

    for workout_type, stats in type_stats.items():
        count = stats['count']
        percentage = (count / total_workouts) * 100
        avg_duration = stats['total_duration'] / count
        avg_calories = stats['total_calories'] / count



        print(f" {workout_type}: {count} тренировок ({percentage:.1f}%)")
        print(f" Средняя длительность: {avg_duration:.0f} мин")
        print(f" Средние калории: {avg_calories:.0f} ккал")
        print()



