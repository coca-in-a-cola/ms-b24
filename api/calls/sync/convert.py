from munch import Munch
from enum import Enum, auto

class EntityType(Enum):
    TASK = 'task'

class Convert:

    def to_b24(entity, type : EntityType):

        if type == EntityType.TASK:
            return Munch(
                UF_MS_HREF = entity.meta.href,
                # Будем считать, что заголовок - это первое предложение задачи
                TITLE = re.split(r', |_|-|! |\. ', entity.description)[0],
                DESCRIPTION = entity.description,
                CREATED_DATE = entity.created,
                CHANGED_DATE = entity.updated,
                STATUS =  5 if entity.done else 1,
                DEADLINE = entity.dueToDate if hasattr(entity, 'dueToDate') else None,
                CREATED_BY = fetchB24UserFromMeta(entity.author.meta).ID,
                RESPONSIBLE_ID = fetchB24UserFromMeta(entity.assignee.meta).ID
                #TODO: дописать ещё поля
            )
    

    def to_ms(entity, type: EntityType):
        pass