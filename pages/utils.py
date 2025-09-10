from dash import no_update

def with_loading(func):
    """
    Decorator برای توابع طولانی
    """
    def wrapper(input_value, status):
        if status.get("running"):
            return no_update, no_update, status  # قبلا در حال اجراست

        # وضعیت شروع اجرای تابع
        status["running"] = True
        try:
            result = func(input_value)  # اجرای تابع واقعی
            status["running"] = False
            success = True
        except:
            result = "Error"
            status["running"] = False
            success = False

        return result, success, status
    return wrapper
