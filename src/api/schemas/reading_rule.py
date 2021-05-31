from src.extensions import ma, db
from src.models import ReadingRule
from .sensor import SensorSchema
from .server import ServerSchema


class ReadingRuleSchema(ma.SQLAlchemyAutoSchema):
    id = ma.Int(dump_only=True)
    server = ma.Nested(ServerSchema)
    sensor = ma.Nested(SensorSchema)

    sensor_id = ma.Int(load_only=True)
    server_id = ma.Int(load_only=True)

    class Meta:
        model = ReadingRule
        sqla_session = db.session
        load_instance = True
