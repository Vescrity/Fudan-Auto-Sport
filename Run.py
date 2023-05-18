import sched
import threading
from sport_api import *
from playground import playgrounds
import time
from argparse import ArgumentParser
import random
import os
import sys


scheduler = sched.scheduler(time.time, time.sleep)


def set_token(token):
    os.environ['FUDAN_SPORT_TOKEN'] = token
    print(f"FUDAN_SPORT_TOKEN 环境变量已设置为：{token}")


def set_id(token):
    os.environ['USER_ID'] = token
    print(f"USER_ID 环境变量已设置为：{token}")


def Run_task(rtid):
    distance = 1200
    distance += random.uniform(-5.0, 25.0)
    total_time = 360
    total_time += random.uniform(-10.0, 10.0)
    selected_route = None
    routes = get_routes()
    for route in routes:
        if route.id == rtid:
            selected_route = route

    sleep_time = random.randint(0, 40)
    time.sleep(sleep_time)
    automator = FudanAPI(selected_route)
    playground = playgrounds[rtid]
    current_distance = 0
    automator.start()
    print(f"START: {selected_route.name}")
    while current_distance < distance:
        try:
            current_distance += distance / total_time
            message = automator.update(playground.random_offset(current_distance))
            print(f"UPDATE: {message} ({current_distance}m / {distance}m)")
            time.sleep(1)
        except:
            continue
    finish_message = automator.finish(playground.coordinate(distance))
    print(f"FINISHED: {finish_message}")


def task_a():
    Run_task(28)


def task_b():
    Run_task(33)


def task_c():
    Run_task(38)


def schedule_task():
    now = time.localtime()
    hour = now.tm_hour
    mint = now.tm_min
    while True:
        try:
            if hour == 7 and mint<15:
                task_a()

            elif hour == 16:
                task_b()

            elif hour == 20:
                task_c()
            if hour < 7:
                next_time = time.mktime((now.tm_year, now.tm_mon,
                                         now.tm_mday, 7, 0, 0, 0, 0, 0))
            elif hour < 16:
                next_time = time.mktime((now.tm_year, now.tm_mon,
                                         now.tm_mday, 16, 0, 0, 0, 0, 0))
            elif hour < 20:
                next_time = time.mktime((now.tm_year, now.tm_mon,
                                         now.tm_mday, 20, 0, 0, 0, 0, 0))
            else:
                next_time = time.mktime((now.tm_year, now.tm_mon,
                                         now.tm_mday + 1, 7, 0, 0, 0, 0, 0))

            delay = next_time - time.time()

    # 执行下一次任务
            scheduler.enter(delay, 1, schedule_task)
        except:
            time.sleep(3)
            continue

    # 下一次任务执行时间为明天 7 点或 16 点


def process_command(command):
    if command.startswith("run a"):
        threading.Thread(target=task_a, daemon=True).start()
    if command.startswith("run b"):
        threading.Thread(target=task_b, daemon=True).start()
    if command.startswith("run c"):
        threading.Thread(target=task_c, daemon=True).start()
    elif command.startswith("set_t "):
        token = command[6:].strip()
        set_token(token)
    elif command.startswith("set_i "):
        token = command[6:].strip()
        set_id(token)
    elif command.startswith("help"):
        print('run a/b/c 执行早操/课外活动/夜跑')
        print('set_i 设置用户id')
        print('set_t 设置token')
    else:
        print("无法识别的命令")


def command_thread():
    while True:
        sys.stdin.close()
        sys.stdin = open(0)
        command = input("请输入命令：")
        process_command(command)


# 启动命令线程
threading.Thread(target=command_thread, daemon=True).start()

# 启动定时任务
schedule_task()
scheduler.run()
