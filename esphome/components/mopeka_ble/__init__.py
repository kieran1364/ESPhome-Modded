import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import esp32_ble_tracker
from esphome.const import CONF_ID

CODEOWNERS = ["@spbrogan"]
DEPENDENCIES = ["esp32_ble_tracker"]

mopeka_ble_ns = cg.esphome_ns.namespace("mopeka_ble")
MopekaListener = mopeka_ble_ns.class_(
    "MopekaListener", esp32_ble_tracker.ESPBTDeviceListener
)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(MopekaListener),
    }
).extend(esp32_ble_tracker.ESP_BLE_DEVICE_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await esp32_ble_tracker.register_ble_device(var, config)
