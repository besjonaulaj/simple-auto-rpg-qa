from main import Fighter

def test_hero_death():
    print("[TEST] Checking if hero dies at 0 HP...")
    test_hero = Fighter("Test", hp=0, attack=10, gold=0)
    if not test_hero.is_alive():
        print("✅ PASS: Hero is correctly marked as dead.")
    else:
        print("❌ FAIL: Hero should be dead at 0 HP.")

if __name__ == "__main__":
    test_hero_death()