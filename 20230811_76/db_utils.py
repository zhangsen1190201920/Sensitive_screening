from models import *
from shared_variable import db

# 根据属性列表生成建表语句
def create_table_sql(table_name, attrs):
    sql = "CREATE TABLE IF NOT EXISTS `{0}` (".format(table_name)
    sql += "`id` INT(11) NOT NULL AUTO_INCREMENT , PRIMARY KEY (`id`),"
    for attr in attrs:
        sql += "`" + attr + "` varchar(100),"
    sql = sql[:-1] + ");"
    return sql


# 这里用于生成建表语句
if __name__ == '__main__':
    data_unit = ReturnValueDataUnit(None)
    attrs = vars(data_unit)
    print(attrs)
    sql = create_table_sql(data_unit.tablename, attrs.keys())
    print(sql)




def query_fs(fs_id):
    sql = "select * from file_subscribe where filesubscribe_id={0}".format(str(fs_id))
    results = list(db.session.execute(sql))
    if len(results) == 0:
        print("query_fs:获取文件订阅规则失败")
        return None
    return FileSubscribeDo(results[0])


def query_all_fs():
    sql = "select * from file_subscribe"
    fs_dict = {}
    results = list(db.session.execute(sql))
    for res in results:
        fs = FileSubscribeDo(res)
        fs_dict[fs.filesubscribe_id] = fs
    return fs_dict


def query_sm(sm_id):
    sql = "select * from sensitive_model where model_id={0}".format(str(sm_id))
    results = list(db.session.execute(sql))
    if len(results) == 0:
        print("query_sm:获取敏感模型失败")
        return None
    return SensitiveModelDo(results[0])


def query_all_sm():
    sql = "select * from sensitive_model"
    sm_dict = {}
    results = list(db.session.execute(sql))
    for res in results:
        sm = SensitiveModelDo(res)
        sm_dict[sm.model_id] = sm
    return sm_dict


def query_all_csemp():
    sql = "select * from csemp"
    csemp_dict = {}
    results = list(db.session.execute(sql))
    for res in results:
        csemp = Csemp(res)
        csemp_dict[csemp.monitor_id] = csemp
    return csemp_dict


# 根据文件订阅id查询敏感模型id
def query_model_id_by_fs(fs_id):
    sql = "select model_id from file_model_assc where filesubscribe_id={}".format(fs_id)
    results = list(db.session.execute(sql))
    return results


# 根据敏感模型id查询文件订阅id
def query_fs_by_model_id(model_id):
    sql = "select filesubscribe_id from file_model_assc where model_id={}".format(model_id)
    results = list(db.session.execute(sql))
    return results


def query_sm_by_csemp_rule_id(rule_id):
    sql = "select model_id from content_model_assc where monitor_id={}".format(rule_id)
    results = list(db.session.execute(sql))
    return results


# 获取table当前最大id
def query_max_id(table):
    sql = "select max(id) from %s" % table
    results = list(db.session.execute(sql))
    return results[0][0]


# 下面的函数用于生成sql语句
def read(table, kwargs):
    """ Generates SQL for a SELECT statement matching the kwargs passed. """
    sql = list()
    sql.append("SELECT * FROM %s " % table)
    if kwargs:
        sql.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.items()))
    sql.append(";")
    return "".join(sql)


def upsert(table, kwargs):
    """ update/insert rows into objects table (update if the row already exists)
        given the key-value pairs in kwargs """
    keys = ["%s" % k for k in kwargs]
    values = ["'%s'" % v for v in kwargs.values()]
    sql = list()
    sql.append("INSERT INTO %s (" % table)
    sql.append(", ".join(keys))
    sql.append(") VALUES (")
    sql.append(", ".join(values))
    sql.append(")")
    #sql.append(") ON DUPLICATE KEY UPDATE ")
    #sql.append(", ".join("%s = '%s'" % (k, v) for k, v in kwargs.items()))
    sql.append(";")
    return "".join(sql)


def delete(table, kwargs):
    """ deletes rows from table where **kwargs match """
    sql = list()
    sql.append("DELETE FROM %s " % table)
    sql.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.items()))
    sql.append(";")
    return "".join(sql)
