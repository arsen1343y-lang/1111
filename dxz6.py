import inspect
import colorama


def introspect_object(obj, name="colorama"):
    print("=" * 60)
    print(f"ІНТРОСПЕКЦІЯ ОБ'ЄКТА: {name}")
    print(f"Тип: {type(obj)}")
    print(f"Документація: {inspect.getdoc(obj)}")
    print("=" * 60)

    public_attrs = [attr for attr in dir(obj) if not attr.startswith("__")]

    for attr in public_attrs:
        value = getattr(obj, attr)
        attr_type = type(value).__name__
        is_func = callable(value)
        print(f"• {attr:<15} | тип: {attr_type:<18} | callable: {is_func}")


if __name__ == "__main__":
    introspect_object(colorama, "colorama")

    for sub_name in ["Fore", "Back", "Style", "init", "deinit", "just_fix_windows_console"]:
        if hasattr(colorama, sub_name):
            sub_obj = getattr(colorama, sub_name)
            print(f"\n--- Атрибути та методи {sub_name} ---")
            sub_attrs = [a for a in dir(sub_obj) if not a.startswith("__")]
            print(sub_attrs[:15])