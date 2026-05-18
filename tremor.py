import cyberpi
import mbot2
import time

# ==========================================================
# 設定：Subject 9 臨床データ（6.68Hz / 無限ループ版）
# ==========================================================
freq = 6.68
# 1周期(約0.15秒)を4工程で分割
step_time = (1.0 / freq) / 4.0 

power = 45 

def start_simulation():
    cyberpi.display.clear()
    cyberpi.display.show_label("Continuous: Subj 9", 16, 0, 0)
    
    # --- 開始時の角度を「床（0度）」として記憶 ---
    try:
        base_angle = mbot2.EM_get_angle("EM1")
    except:
        base_angle = 0
    
    try:
        # 【変更点】時間制限をなくし、True（無限）に設定
        while True:
            
            # --- 1. 稼働（0度から45度方向へ） ---
            mbot2.EM_set_speed(-power, "EM1")
            mbot2.EM_set_speed(power, "EM2")
            time.sleep(step_time)
            
            # --- 2. ブレーキ ---
            mbot2.EM_set_speed(0, "all")
            time.sleep(step_time / 2)
            
            # --- 3. 戻り（0度方向へ）＋ マイナス進入防止チェック ---
            back_start = time.time()
            while time.time() - back_start < step_time:
                try:
                    current = mbot2.EM_get_angle("EM1")
                    # 開始位置（0度）に戻ったら戻り動作を即座に終了
                    if current >= base_angle: 
                        break
                except:
                    pass
                
                mbot2.EM_set_speed(power, "EM1")
                mbot2.EM_set_speed(-power, "EM2")
            
            # --- 4. ブレーキ（0度地点で停止） ---
            mbot2.EM_set_speed(0, "all")
            time.sleep(step_time / 2)
            
            # 【重要】ループ中にBボタンが押されたら終了する
            if cyberpi.controller.is_press('b'):
                break
                
    except Exception as e:
        cyberpi.display.clear()
        cyberpi.display.show_label("ERROR!", 16, 0, 0)
        cyberpi.display.show_label(str(e), 12, 0, 30)
        while not cyberpi.controller.is_press('b'):
            pass

    # 停止処理
    mbot2.motor_stop("all")
    mbot2.EM_set_speed(0, "all")
    cyberpi.display.clear()
    cyberpi.display.show_label("Stopped / A:Start", 16, 0, 0)

# ==========================================================
# メインループ
# ==========================================================
cyberpi.display.show_label("A: START (Infinite)", 16, 0, 0)

while True:
    if cyberpi.controller.is_press('a'):
        start_simulation()
    
    if cyberpi.controller.is_press('b'):
        mbot2.motor_stop("all")