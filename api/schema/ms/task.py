from marshmallow import Schema, fields
from api.schema.ms.meta import MetaSchema


class TaskSchema(MetaSchema):
    accountId = fields.UUID()
    '''
    ID учетной записи Кассира
    '''


    agent = fields.Nested(MetaSchema)
    '''
    Метаданные Контрагента или юрлица, связанного с задачей.
    Задача может быть привязана либо к конрагенту, либо к юрлицу, либо к документу
    '''


    assignee = fields.Nested(MetaSchema, required=True)
    '''
    Метаданные ответственного за выполнение задачи \n
    Необходимо при создании
    '''


    author = fields.Nested(MetaSchema)
    '''
    Метаданные Сотрудника, создавшего задачу (администратор аккаунта, если автор - Приложение) \n
    Обязательное при ответе Только для чтения Expand
    '''


    authorApplication = fields.Nested(MetaSchema)
    '''
    Метаданные Приложения, создавшего задачу \n
    Только для чтения
    '''


    completed = fields.DateTime()
    '''
    Время выполнения задачи \n
    Обязательное при ответе, Только для чтения
    '''


    created = fields.DateTime()
    '''
    Момент создания \n
    Обязательное при ответе, Только для чтения
    '''


    description = fields.String(required=True)
    '''
    Текст задачи \n
    Обязательное при ответе, Необходимо при создании
    '''


    done = fields.Bool()
    '''
    Отметка о выполнении задачи \n
    Обязательное при ответе
    '''


    dueToDate = fields.DateTime()
    '''
    Срок задачи
    '''


    files = fields.Nested(MetaSchema, many=True)
    '''
    Метаданные массива Файлов (Максимальное количество файлов - 100) \n
    Обязательное при ответе, Expand
    '''


    id = fields.UUID()
    '''
    ID Задачи \n
    Обязательное при ответе, Только для чтения
    '''


    implementer = fields.Nested(MetaSchema)
    '''
    Метаданные Сотрудника, выполнившего задачу \n
    Только для чтения, Expand
    '''


    #meta = fields.Nested(MetaSchema)
    '''
    Метаданные Задачи \n
    Обязательное при ответе
    (наследуется от класса MetaSchema)
    '''


    notes = fields.Nested(MetaSchema)
    '''
    Метаданные комментария к задаче \n
    Обязательное при ответе, Expand
    '''


    operation = fields.Nested(MetaSchema)
    '''
    Метаданные Документа, связанного с задачей.
    Задача может быть привязана либо к конрагенту, либо к юрлицу, либо к документу \n
    Expand
    '''


    updated = fields.DateTime()
    '''
    Момент последнего обновления Задачи \n
    Обязательное при ответе, Только для чтения
    '''