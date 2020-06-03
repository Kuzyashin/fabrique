from drf_yasg.utils import swagger_auto_schema


def polls_list_schema():
    return swagger_auto_schema(
        operation_id='Get polls list',
        operation_summary="Получение списка опросов",
        operation_description="Для неавторизованных/не суперюзеров выдаст список `АКТИВНЫХ` опросов.\n"
                              "Для суперюзера выдаст список `ВСЕХ` опросов\n\n"
    )


def polls_retrieve_schema():
    return swagger_auto_schema(
        operation_id='Get single poll',
        operation_summary="Получение опросa",
        operation_description="Для неавторизованных/не суперюзеров работает для `АКТИВНЫХ` опросов.\n"
                              "Для суперюзера работает для `ВСЕХ` опросов"
    )


def polls_create_schema():
    return swagger_auto_schema(
        operation_id='Create poll',
        operation_summary="Cоздание опросa",
        operation_description="Доступно только для суперюзера"
    )


def polls_update_schema():
    return swagger_auto_schema(
        operation_id='Update poll',
        operation_summary="Обновление опросa",
        operation_description="Доступно только для суперюзера"
    )


def poll_question_list_schema():
    return swagger_auto_schema(
        operation_id='Get question list',
        operation_summary="Получение вопросов",
        operation_description="Работает только для суперюзера"
    )


def poll_question_retrieve_schema():
    return swagger_auto_schema(
        operation_id='Get single question',
        operation_summary="Получение вопроса",
        operation_description="Работает только для суперюзера"
    )


def poll_question_create_schema():
    return swagger_auto_schema(
        operation_id='Create question',
        operation_summary="Создание вопроса",
        operation_description="Работает только для суперюзера"
    )


def poll_question_update_schema():
    return swagger_auto_schema(
        operation_id='Update question',
        operation_summary="Обновление вопроса",
        operation_description="Работает только для суперюзера"
    )


def question_answer_list_schema():
    return swagger_auto_schema(
        operation_id='Get answer list',
        operation_summary="Получение вариантов ответов",
        operation_description="Работает только для суперюзера"
    )


def question_answer_retrieve_schema():
    return swagger_auto_schema(
        operation_id='Get single answer',
        operation_summary="Получение варианта ответа",
        operation_description="Работает только для суперюзера"
    )


def question_answer_create_schema():
    return swagger_auto_schema(
        operation_id='Create answer',
        operation_summary="Создание варианта ответа",
        operation_description="Работает только для суперюзера"
    )


def question_answer_update_schema():
    return swagger_auto_schema(
        operation_id='Update answer',
        operation_summary="Обновление варианта ответа",
        operation_description="Работает только для суперюзера"
    )


def poll_answer_list_schema():
    return swagger_auto_schema(
        operation_id='Get all poll answers',
        operation_summary="Получение ответов по опросам",
        operation_description="Работает только для суперюзера\n"
                              "Есть возможность фильтровать по параметру `?user_id=`"
    )


def poll_answer_retrieve_schema():
    return swagger_auto_schema(
        operation_id='Get single poll answer',
        operation_summary="Получение ответа по опросу",
        operation_description="Работает только для суперюзера\n"
    )


def poll_answer_create_schema():
    return swagger_auto_schema(
        operation_id='Create poll answer',
        operation_summary="Создание ответа по опросу",
        operation_description="Доступно всем пользователям, если пользорватель не авторизован, "
                              "будет использовано `null`\n"
    )