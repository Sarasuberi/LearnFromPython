from datetime import datetime
from loguru import logger

# 添加到文件
dateTime = datetime.now().strftime("%Y-%m-%d")
logger.remove()

# add的参数logger.add("保存文件地址和名字"，等级，格式，限定文件大小，保存时间，压缩，异步）)
logger.add(f"loginfo\{dateTime}.log", level="ERROR",format="{time} {level} {message}",rotation="100 MB", retention="10 days", compression="zip", enqueue=True)

# 可以删除某个特定的handler_id
# logger.remove(handler_id)

# 严重程度依次递增
logger.trace("trace msg")
logger.debug("debug msg")
logger.info("info msg")
logger.success("success msg")
logger.warning("warning msg")
logger.error("error msg")
logger.critical("critical msg")

# 抓取异常报警信息
logger.exception("exception msg")
