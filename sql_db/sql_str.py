#######################################
# PMS/BBS
SQL_CREATE_PMS_OUT_MAIL_TAB = ("CREATE TABLE pms_out_msg (\n"
                               "`MID` INT(6) AUTO_INCREMENT NOT NULL,\n"
                               "`BID` varchar(12),\n"
                               "`from_call` VARCHAR(10) NOT NULL,\n"
                               "`from_bbs` VARCHAR(40) NULL,\n"
                               "`from_bbs_call` VARCHAR(100) NULL,\n"
                               "`to_call` varchar(10) NOT NULL,\n"
                               "`to_bbs` varchar(40) NULL,\n"
                               "`to_bbs_call` varchar(10) NULL,\n"
                               "`size` BIGINT UNSIGNED NULL,\n"
                               "`subject` varchar(100) NULL,\n"
                               "`header` BLOB,\n"
                               "`msg` LONGBLOB,\n"
                               # "`sent_to` VARCHAR(202) DEFAULT '[]' NULL,\n"
                               "`time` varchar(30) NULL,\n"
                               "`tx_time` varchar(30) NULL,\n"
                               "`utctime` varchar(30) NULL,\n"
                               "`type` varchar(1) NOT NULL,\n"
                               "`flag` varchar(2) DEFAULT 'E' ,\n"
                               "PRIMARY KEY (MID)\n"
                               ");\n")

SQLITE_CREATE_PMS_OUT_MAIL_TAB = ("CREATE TABLE pms_out_msg (\n"
                                  "`MID` INTEGER PRIMARY KEY AUTOINCREMENT,\n"
                                  "`BID` varchar(12),\n"
                                  "`from_call` VARCHAR(10) NOT NULL,\n"
                                  "`from_bbs` VARCHAR(40) NULL,\n"
                                  "`from_bbs_call` VARCHAR(100) NULL,\n"
                                  "`to_call` varchar(10) NOT NULL,\n"
                                  "`to_bbs` varchar(40) NULL,\n"
                                  "`to_bbs_call` varchar(10) NULL,\n"
                                  "`size` BIGINT UNSIGNED NULL,\n"
                                  "`subject` varchar(100) NULL,\n"
                                  "`header` BLOB,\n"
                                  "`msg` LONGBLOB,\n"
                                  # "`sent_to` VARCHAR(202) DEFAULT '[]' NULL,\n"
                                  "`time` varchar(30) NULL,\n"
                                  "`tx_time` varchar(30) NULL,\n"
                                  "`utctime` varchar(30) NULL,\n"
                                  "`type` varchar(1) NOT NULL,\n"
                                  "`flag` varchar(2) DEFAULT 'E'\n"
                                  ");\n")

SQL_CREATE_PMS_FWD_TASK_TAB = ("CREATE TABLE pms_fwd_q (\n"
                               "`FWDID` varchar(20) NOT NULL,\n"
                               "`BID` varchar(12) NOT NULL,\n"
                               "`MID` INT NOT NULL,\n"
                               "`from_call` varchar(10) NOT NULL,"
                               "`from_bbs` varchar(40) NOT NULL,"
                               "`from_bbs_call` varchar(10) NOT NULL,"
                               "`to_call` varchar(10) NOT NULL,"
                               "`to_bbs` varchar(40) NOT NULL,"
                               "`to_bbs_call` varchar(10) NOT NULL,"
                               "`fwd_bbs_call` varchar(10) NOT NULL,"
                               "`size` BIGINT UNSIGNED NULL,\n"
                               "`subject` varchar(100) NULL,\n"
                               "`type` varchar(1) NOT NULL,\n"
                               "`flag` varchar(2) DEFAULT 'F' NOT NULL,\n"
                               "`try` TINYINT DEFAULT 0,\n"
                               "`tx_time` varchar(30) NULL,\n"
                               "PRIMARY KEY (FWDID)\n"
                               ");\n"
                               )

SQL_CREATE_PMS_IN_MAIL_TAB = ("CREATE TABLE pms_in_msg (\n"
                              "	`MSGID` int NOT NULL AUTO_INCREMENT,\n"
                              "	`BID` varchar(20) NOT NULL,\n"
                              "	`from_call` VARCHAR(100) NOT NULL,\n"
                              "	`from_bbs` VARCHAR(100) NULL,\n"
                              "	`to_call` varchar(100) NOT NULL,\n"
                              "	`to_bbs` varchar(100) NULL,\n"
                              "	`size` BIGINT UNSIGNED NULL,\n"
                              "	`subject` varchar(100) NULL,\n"
                              "	`header` BLOB,\n"
                              "	`msg` LONGBLOB,\n"
                              "	`path` VARCHAR(2048) NULL,\n"
                              "	`time` varchar(30) NULL,\n"
                              "	`rx_time` varchar(30) NULL,\n"
                              "	`new` TINYINT(1) DEFAULT 1 NOT NULL,\n"
                              " `flag` varchar(2) DEFAULT 'IN' NOT NULL,\n"
                              " `typ` varchar(2) NOT NULL,\n"
                              "	PRIMARY KEY (MSGID)\n"
                              ");\n")

SQLITE_CREATE_PMS_IN_MAIL_TAB = ("CREATE TABLE pms_in_msg (\n"
                              "	`MSGID` INTEGER PRIMARY KEY AUTOINCREMENT,\n"
                              "	`BID` varchar(20) NOT NULL,\n"
                              "	`from_call` VARCHAR(100) NOT NULL,\n"
                              "	`from_bbs` VARCHAR(100) NULL,\n"
                              "	`to_call` varchar(100) NOT NULL,\n"
                              "	`to_bbs` varchar(100) NULL,\n"
                              "	`size` BIGINT UNSIGNED NULL,\n"
                              "	`subject` varchar(100) NULL,\n"
                              "	`header` BLOB,\n"
                              "	`msg` LONGBLOB,\n"
                              "	`path` VARCHAR(2048) NULL,\n"
                              "	`time` varchar(30) NULL,\n"
                              "	`rx_time` varchar(30) NULL,\n"
                              "	`new` TINYINT(1) DEFAULT 1 NOT NULL,\n"
                              " `flag` varchar(2) DEFAULT 'IN' NOT NULL,\n"
                              " `typ` varchar(2) NOT NULL\n"
                              ");\n")


SQL_CREATE_FWD_PATHS_TAB = ("CREATE TABLE fwdPaths (\n"
                            "`path` varchar(300) NOT NULL,\n"
                            "destBBS varchar(30) NOT NULL,\n"
                            "fromBBS varchar(30) NOT NULL,\n"
                            "hops TINYINT DEFAULT 0 NOT NULL,\n"
                            "destR1 varchar(10) NULL,\n"
                            "destR2 varchar(10) NULL,\n"
                            "destR3 varchar(10) NULL,\n"
                            "destR4 varchar(10) NULL,\n"
                            "destR5 varchar(10) NULL,\n"
                            "destR6 varchar(10) NULL,\n"
                            "lastUpdate varchar(30) NOT NULL,\n"
                            "PRIMARY KEY (`path`)\n"
                            ");\n")

SQL_CREATE_FWD_NODES_TAB = ("CREATE TABLE fwdNodes (\n"
                            "`node` varchar(10) NOT NULL,\n"
                            "Address varchar(30) NULL,\n"
                            "destR1 varchar(10) NULL,\n"
                            "destR2 varchar(10) NULL,\n"
                            "destR3 varchar(10) NULL,\n"
                            "destR4 varchar(10) NULL,\n"
                            "destR5 varchar(10) NULL,\n"
                            "destR6 varchar(10) NULL,\n"
                            "locator varchar(8) NULL,\n"
                            "lastUpdate varchar(30) NOT NULL,\n"
                            "PRIMARY KEY (`node`)\n"
                            ");\n")
SQL_GET_LAST_MSG_ID = "SELECT MID FROM pms_out_msg ORDER BY MID DESC LIMIT 1;"
SQL_BBS_OUT_MAIL_TAB_IS_EMPTY = "SELECT CASE WHEN EXISTS(SELECT 1 FROM pms_out_msg) THEN 0 ELSE 1 END AS IsEmpty;"


#######################################
# APRS
SQL_CREATE_APRS_WX_TAB = ("CREATE TABLE APRSwx (\n"
                          "`ID` INT(255) UNSIGNED AUTO_INCREMENT NOT NULL,\n"
                          "`from_call` varchar(9) NOT NULL,\n"
                          "`to_call` varchar(9) NOT NULL,\n"
                          "`via` varchar(9),\n"
                          "`path` varchar(100) NOT NULL,\n"
                          "`port_id` varchar(6) NOT NULL,\n"
                          "`symbol` varchar(2),\n"
                          "`symbol_table` varchar(2),\n"
                          "`locator` varchar(8),\n"
                          "`distance` varchar(8),\n"
                          "`latitude` varchar(9),\n"
                          "`longitude` varchar(9),\n"
                          "`pressure` varchar(8) DEFAULT '',\n"
                          "`humidity` varchar(5) DEFAULT '',\n"
                          "`rain_1h` varchar(8) DEFAULT '',\n"
                          "`rain_24h` varchar(8) DEFAULT '',\n"
                          "`rain_since_midnight` varchar(8) DEFAULT '',\n"
                          "`temperature` varchar(5) DEFAULT '',\n"
                          "`wind_direction` varchar(8) DEFAULT '',\n"
                          "`wind_gust` varchar(8) DEFAULT '',\n"
                          "`wind_speed` varchar(8) DEFAULT '',\n"
                          "`luminosity` varchar(8) DEFAULT '',\n"
                          "`raw_timestamp` varchar(10) NOT NULL,\n"
                          "`rx_time` varchar(19) NOT NULL,\n"
                          "`comment` varchar(200) DEFAULT '', \n"
                          "PRIMARY KEY (ID)\n"
                          ");\n")

SQLITE_CREATE_APRS_WX_TAB = SQL_CREATE_APRS_WX_TAB.replace(
    "`ID` INT(255) UNSIGNED AUTO_INCREMENT NOT NULL,",
    "`ID` INTEGER PRIMARY KEY AUTOINCREMENT,"
).replace(
    ", \nPRIMARY KEY (ID)\n",
    ""
)

#######################################
# PortStatistik
SQL_CREATE_PORT_STATISTIK_TAB = ("CREATE TABLE `PortStatistic`(\n"
                                 "`ID` INT(255) UNSIGNED AUTO_INCREMENT NOT NULL,"
                                 "`time` varchar(19) NOT NULL,\n"
                                 "`port_id` TINYINT(255) UNSIGNED NOT NULL,\n"
                                 "`N_pack` SMALLINT(255) UNSIGNED DEFAULT 0,\n"
                                 "`I` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`SABM` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`DM` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`DISC` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`REJ` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`SREJ` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`RR` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`RNR` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`UA` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`UI` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`FRMR` INT(255) UNSIGNED DEFAULT 0,\n"
                                 
                                 "`n_I` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`n_SABM` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`n_DM` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`n_DISC` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`n_REJ` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`n_SREJ` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`n_RR` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`n_RNR` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`n_UA` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`n_UI` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`n_FRMR` INT(255) UNSIGNED DEFAULT 0,\n"
                                 
                                 "`DATA_W_HEADER` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "`DATA` INT(255) UNSIGNED DEFAULT 0,\n"
                                 "PRIMARY KEY (`ID`)\n"
                                 ");\n")

SQLITE_CREATE_PORT_STATISTIK_TAB = ("CREATE TABLE `PortStatistic`(\n"
                                    "`ID` INTEGER PRIMARY KEY AUTOINCREMENT,\n"
                                    "`time` varchar(19) NOT NULL,\n"
                                    "`port_id` UNSIGNED TINYINT(255) NOT NULL,\n"
                                    "`N_pack` UNSIGNED SMALLINT(255) DEFAULT 0,\n"
                                    "`I` UNSIGNED INT(255) DEFAULT 0,\n"
                                    
                                    "`SABM` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`DM` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`DISC` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`REJ` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`SREJ` UNSIGNED INT(255) DEFAULT 0,\n"
                                    
                                    "`RR` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`RNR` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`UA` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`UI` UNSIGNED INT(255)  DEFAULT 0,\n"
                                    "`FRMR` UNSIGNED INT(255) DEFAULT 0,\n"
                                    
                                    "`n_I` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`n_SABM` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`n_DM` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`n_DISC` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`n_REJ` UNSIGNED INT(255) DEFAULT 0,\n"
                                    
                                    "`n_SREJ` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`n_RR` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`n_RNR` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`n_UA` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`n_UI` UNSIGNED INT(255)  DEFAULT 0,\n"
                                    
                                    "`n_FRMR` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`DATA_W_HEADER` UNSIGNED INT(255) DEFAULT 0,\n"
                                    "`DATA` UNSIGNED INT(255) DEFAULT 0\n"
                                    ");\n")
"""
SQLITE_CREATE_PORT_STATISTIK_TAB = SQL_CREATE_PORT_STATISTIK_TAB.replace(
    "`time` varchar(19) NOT NULL,",
    "`time` varchar(19)  PRIMARY KEY NOT NULL,",
).replace(
    ", \nPRIMARY KEY (`time`)\n",
    ""
)
"""

#######################################
# UserDB
"""
SQL_CREATE_USERDB_TAB = ("CREATE TABLE user_db ("
                              "	`call_str` varchar(9),"
                              "	`Call` VARCHAR(6) NOT NULL,"
                              "	`SSID` TINYINT(15) UNSIGNED DEFAULT 0,"
                              "	`Alias` VARCHAR(6) NULL,"
                              "	`TYP` varchar(15) NULL,"
                              "	`Name` varchar(20) NULL,"
                              "	`Land` varchar(30) NULL,"
                              "	`ZIP` varchar(10) NULL,"
                              "	`QTH` varchar(40) NULL,"
                              "	`LOC` varchar(8) NULL,"
                              "	`Lat` varchar(10) DEFAULT '0',"
                              "	`Lon` varchar(10) DEFAULT '0',"
                              "	`Distance` int UNSIGNED DEFAULT 0,"
                              "	`Language` TINYINT DEFAULT -1,"
                              "	`PRmail` varchar(30) NULL,"
                              "	`Email` varchar(40) NULL,"
                              "	`HTTP` varchar(50) NULL,"
                              "	`Info` varchar(5000) NULL,"
                              "	`NODE` varchar(100) DEFAULT '[]',"
                              "	`BBS` varchar(100) DEFAULT '[]',"
                              "	`Other` varchar(100) DEFAULT '[]',"
                              "	`Sysop_Call` varchar(9) NULL,"
                              "	`via_NODE_HF` varchar(9) NULL,"
                              "	`via_NODE_AXIP` varchar(9) NULL,"
                              "	`AXIP` varchar(40) DEFAULT ' None , 0',"
                              "	`Software` varchar(30) NULL,"
                              "	`Encoding` varchar(10) DEFAULT 'CP437',"
                              "	`last_edit` varchar(25) NULL,"
                              "	`last_seen` varchar(25) NULL,"
                              "	`Connects` int UNSIGNED DEFAULT 0,"
                              "	`pac_len` int(9) UNSIGNED DEFAULT 0,"
                              "	`max_pac` int(4) UNSIGNED DEFAULT 0,"
                              "	`CText` varchar(2000) NULL,"
                              "	`routes` varchar(2000) DEFAULT '[]',"
                              "	`software_str` varchar(30) NULL,"
                              "	`sys_pw` varchar(160) NULL,"
                              "	`sys_pw_autologin` TINYINT(1) UNSIGNED DEFAULT 0,"
                              "	`sys_pw_parm` varchar(20) DEFAULT '[5, 80, ''SYS'']',"
                              " PRIMARY KEY (`call_str`)"
                              ");")

SQLITE_CREATE_USERDB_TAB = ("CREATE TABLE user_db ("
                              "	`call_str` varchar(9) PRIMARY KEY NOT NULL,"
                              "	`Call` VARCHAR(6) NOT NULL,"
                              "	`SSID` UNSIGNED TINYINT(15) DEFAULT 0,"
                              "	`Alias` VARCHAR(6) NULL,"
                              "	`TYP` varchar(15) NULL,"
                              "	`Name` varchar(20) NULL,"
                              "	`Land` varchar(30) NULL,"
                              "	`ZIP` varchar(10) NULL,"
                              "	`QTH` varchar(40) NULL,"
                              "	`LOC` varchar(8) NULL,"
                              "	`Lat` varchar(10) DEFAULT '0',"
                              "	`Lon` varchar(10) DEFAULT '0',"
                              "	`Distance` UNSIGNED INT DEFAULT 0,"
                              "	`Language` TINYINT DEFAULT -1,"
                              "	`PRmail` varchar(30) NULL,"
                              "	`Email` varchar(40) NULL,"
                              "	`HTTP` varchar(50) NULL,"
                              "	`Info` varchar(5000) NULL,"
                              "	`NODE` varchar(100) DEFAULT '[]',"
                              "	`BBS` varchar(100) DEFAULT '[]',"
                              "	`Other` varchar(100) DEFAULT '[]',"
                              "	`Sysop_Call` varchar(9) NULL,"
                            "	`via_NODE_HF` varchar(9) NULL,"
                              "	`via_NODE_AXIP` varchar(9) NULL,"
                              "	`AXIP` varchar(40) DEFAULT 'None, 0',"
                              "	`Software` varchar(30) NULL,"
                              "	`Encoding` varchar(10) DEFAULT 'CP437',"
                              "	`last_edit` varchar(25) NULL,"
                              "	`last_seen` varchar(25) NULL,"
                              "	`Connects` UNSIGNED int DEFAULT 0,"
                              "	`pac_len` UNSIGNED int(9) DEFAULT 0,"
                              "	`max_pac` UNSIGNED int(4) DEFAULT 0,"
                              "	`CText` varchar(2000) NULL,"
                              "	`routes` varchar(2000) DEFAULT '[]',"
                              "	`software_str` varchar(30) NULL,"
                              "	`sys_pw` varchar(160) NULL,"
                              "	`sys_pw_autologin` UNSIGNED TINYINT(1) DEFAULT 0,"
                              "	`sys_pw_parm` varchar(20) DEFAULT '[5, 80, ''SYS'']'"
                              ");")

"""
#######################################
# MH
"""
SQL_CREATE_MH_TAB = ("CREATE TABLE `MH`(\n"
                     "`call` varchar(9) NOT NULL, \n"
                     "`to_call` varchar(9) NOT NULL, \n"
                     "`route` varchar(200) DEFAULT '', \n"
                     "`port_id` varchar(2) NOT NULL, \n"
                     "`pack_len` varchar(3) DEFAULT '0', \n"
                     "`header_len` varchar(3) DEFAULT '0', \n"
                     "`frame_typ` varchar(4) DEFAULT '', \n"   # 
                     "`frame_pid` varchar(4) DEFAULT '', \n"   # 
                     "`rx_tx` varchar(2) DEFAULT 'rx', \n"   # 
                     "`axip_add` varchar(50) DEFAULT '', \n"
                     "`locator` varchar(8) DEFAULT '', \n"
                     "`distance` varchar(8) DEFAULT '', \n"
                     "`first_seen` varchar(19) NOT NULL, \n"
                     "`last_seen` varchar(19) NOT NULL, \n"
                     "PRIMARY KEY (`call`)\n"
                     ");\n")

SQLITE_CREATE_MH_TAB = SQL_CREATE_MH_TAB
"""
"""
SQLITE_CREATE_MH_TAB = SQL_CREATE_MH_TAB.replace(
    "`ID` INTEGER AUTO_INCREMENT NOT NULL,",
    "`ID` INTEGER PRIMARY KEY AUTOINCREMENT,"
).replace(
    ", \nPRIMARY KEY (ID)\n",
    ""
)
"""
########################################################################
SQL_BBS_TABLES = {
    "pms_in_msg": SQL_CREATE_PMS_IN_MAIL_TAB,
    "fwdPaths": SQL_CREATE_FWD_PATHS_TAB,
    "fwdNodes": SQL_CREATE_FWD_NODES_TAB,
    "pms_out_msg": SQL_CREATE_PMS_OUT_MAIL_TAB,
    "pms_fwd_q": SQL_CREATE_PMS_FWD_TASK_TAB,
}
SQLITE_BBS_TABLES = {
    "pms_in_msg": SQLITE_CREATE_PMS_IN_MAIL_TAB,
    "fwdPaths": SQL_CREATE_FWD_PATHS_TAB,
    "fwdNodes": SQL_CREATE_FWD_NODES_TAB,
    "pms_out_msg": SQLITE_CREATE_PMS_OUT_MAIL_TAB,
    "pms_fwd_q": SQL_CREATE_PMS_FWD_TASK_TAB,
}
USERDB_TABLES = {
    # "user_db": SQL_CREATE_USERDB_TAB,
}
SQLITE_USERDB_TABLES = {
    # "user_db": SQLITE_CREATE_USERDB_TAB,
}
APRS_TABLES = {
    'APRSwx': SQL_CREATE_APRS_WX_TAB
}
SQLITE_APRS_TABLES = {
    'APRSwx': SQLITE_CREATE_APRS_WX_TAB
}
PORT_STATISTIK_TAB = {
    'PortStatistic': SQL_CREATE_PORT_STATISTIK_TAB
}
SQLITE_PORT_STATISTIK_TAB = {
    'PortStatistic': SQLITE_CREATE_PORT_STATISTIK_TAB
}
"""
MH_TABLES = {
    'MH': SQL_CREATE_MH_TAB
}
SQLITE_MH_TABLES = {
    'MH': SQLITE_CREATE_MH_TAB
}
"""
