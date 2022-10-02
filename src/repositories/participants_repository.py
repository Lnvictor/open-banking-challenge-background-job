from documents.participant import Participant
from repositories.nosql_repository import NoSqlRepository


class ParticipantsRepository(NoSqlRepository):
    document = Participant
