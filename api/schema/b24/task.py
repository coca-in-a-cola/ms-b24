from marshmallow import Schema, fields
from api.schema.object import ObjectSchema


class TaskSchema(ObjectSchema):
    title = fields.String(required=True)
    '''
    Название задачи.
    '''


    description = fields.String()
    '''
    Описание задачи.
    '''


    deadline = fields.DateTime()
    '''
    Крайний срок.
    '''


    startDatePlan = fields.DateTime()
    '''
    Плановая дата начала.
    '''


    endDatePlan = fields.DateTime()
    '''
    Плановая дата завершения.
    '''


    priority = fields.Integer()
    '''
    Приоритет
    '''


    accomplices = fields.List(fields.Integer())
    '''
    Соисполнители (идентификаторы пользователей).
    '''


    accomplice = fields.Integer()
    '''
    Соисполнители (поле используется для фильтрации).    
    '''
    

    auditors = fields.List(fields.Integer())
    '''
    Наблюдатели (идентификаторы пользователей).
    '''


    auditor = fields.Integer()
    '''
    Наблюдатели (поле используется для фильтрации).
    '''


    tags = fields.List(fields.String())
    '''
    Теги (при добавлении - просто массив тегов в виде текста). \n
    CTasks::GetList() не возвращает поля тегов. \n
    CTaskItem::getInstance()->getTags() возвращает массив имен тегов.
    '''


    tag = fields.String()
    '''
    Теги (поле используется для фильтрации).
    '''


    allowChangeDeadline = fields.String()
    '''
    Флаг "Разрешить ответственному менять крайний срок".
    '''


    taskControl = fields.String()
    '''
    Флаг "Принять работу после завершения задачи".
    '''


    parentId = fields.Integer()
    '''
    Идентификатор родительской задачи.
    '''


    dependsOn = fields.Integer()
    '''
    Идентификатор предыдущей задачи.
    '''


    groupId = fields.Integer()
    '''
    Идентификатор рабочей группы.
    '''


    responsibleId = fields.Integer()
    '''
    Идентификатор ответственного.
    '''


    timeEstimate = fields.Number()
    '''
    Плановые трудозатраты.
    '''


    id = fields.Integer()
    '''
    Идентификатор задачи. Уникален в рамках базы данных.
    '''


    createdBy = fields.Integer()
    '''
    Идентификатор постановщика.
    '''


    descriptionInBbcode = fields.String()
    '''
    Флаг указывающий, что описание задачи хранится в bb-кодах.
    '''


    declineReason = fields.String()
    '''
    Причина отклонения задачи.
    '''


    realStatus = fields.String()
    '''
    Истинный статус задачи,
    который записывается через status (см. константы CTasks::STATE_xxx).\n
    Только для чтения.
    '''


    status = fields.Integer()
    '''
    Мета-статус задачи.
    При записи можно использовать константы CTasks::STATE_xxx, однако,
    при чтении, помимо CTasks::STATE_xxx, в результатах можно увидеть CTasks::METASTATE_xxx.
    То есть на самом деле статус задачи может быть CTasks::stateNew,
    а при чтении вернется нам CTasks::metastateExpired (для просроченной задачи).
    В случае если мы хотим узнать истинный статус задачи, следует читать поле realStatus.

    Task statuses: 
    1 - New,
    2 - Pending (Accepted),
    3 - In Progress,
    4 - Supposedly completed,
    5 - Completed,
    6 - Deferred,
    7 - Declined
    '''


    responsibleName = fields.String()
    '''
    Имя ответственного.
    '''
    

    responsibleLastName = fields.String()
    '''
    Фамилия ответственного.
    '''


    responsibleSecondName = fields.String()
    '''
    Отчество ответственного.
    '''


    dateStart = fields.DateTime()
    '''
    Дата начала выполнения задачи.
    '''


    durationFact = fields.Integer()
    '''
    Затраченное время на задачу (в минутах).
    '''


    durationPlan = fields.Integer()
    '''
    Планируемая длительность в часах или днях.
    '''


    durationType = fields.String()
    '''
    Тип единицы измерения в планируемой длительности: days, hours или minutes.
    '''


    createdByName = fields.String()
    '''
    Имя постановщика.
    '''


    createdByLastName = fields.String()
    '''
    Фамилия постановщика.
    '''


    createdBySecondName = fields.String()
    '''
    Отчество постановщика.
    '''


    changedBy = fields.Integer()
    '''
    Пользователь, изменивший задачу в последний раз (идентификатор пользователя).
    '''


    changedDate = fields.DateTime()
    '''
    Дата последнего изменения задачи.
    '''


    statusChangedBy = fields.Integer()
    '''
    Пользователь, изменивший статус задачи (идентификатор пользователя).
    '''


    statusChangedDate = fields.DateTime()
    '''
    Дата смены статуса.
    '''


    closedBy = fields.Integer()
    '''
    Кем была завершена задача.
    '''


    closedDate = fields.DateTime()
    '''
    Дата завершения задачи.
    '''


    guid = fields.UUID()
    '''
    Глобально-уникальный идентификатор. \n
    С приемлемым уровнем уверенности, данный идентификатор непреднамеренно никогда
    не будет использован для чего-то ещё даже в других базах данных.
    '''


    mark = fields.String()
    '''
    Оценка по задаче (возможные значения p (положительная) и n (отрицательная)).
    '''


    viewedDate = fields.DateTime()
    '''
    Дата последнего просмотра задачи в публичном интерфейсе текущим пользователем \n
    (от имени которого делается запрос на получение данных задачи).
    '''


    timeSpentInLogs = fields.Integer()
    '''
    Затраченное время на задачу (в секундах).
    '''


    favorite = fields.Boolean()
    '''
    Присутствие и избранном для текущего пользователя.
    '''


    allowTimeTracking = fields.String()
    '''
    Флаг включения учета затраченного времени по задаче.
    '''


    addInReport = fields.String()
    '''
    Флаг включения задачи в отчет по эффективности.
    '''


    forumId = fields.String()
    '''Идентификатор форума , в котором хранятся комментарии к задаче.'''


    forumTopicId = fields.String()
    '''Идентификатор темы форума , в котором хранятся комментарии к задаче.'''


    commentsCount = fields.Integer()
    '''Число комментариев к задаче.'''


    siteId = fields.Integer()
    '''Идентификатор сайта. По умолчанию в это поле записывается идентификатор сайта, на котором создается задача.'''


    subordinate = fields.String()
    '''Флаг, который показывает, является ли кто-то из участников задачи подчиненным текущего пользователя.'''


    forkedByTemplateId = fields.Integer()
    '''Идентификатор шаблона, на основе которого была автоматически создана задача. Для некоторых старых задач может быть не установлен.'''


    multitask = fields.String()
    '''Флаг, означающий, что задача была создана для нескольких ответственных.'''


    onlyRootTasks = fields.String()
    '''Поле, позволяющее выбирать только те задачи, у которых либо нет родительской задачи, либо есть, но к этой родительской задаче мы не имеем доступа.'''


    matchWorkTime = fields.String()
    '''Флаг, который показывает, что даты исполнения и крайний срок должны всегда устанавливаться в рабочее время.'''
    # todo:д описать поля схемы из документации битрикса, переделать их в camelCase,
    # потому что оно возвращает в camelCase, а не так, как в документации