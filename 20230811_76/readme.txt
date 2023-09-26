2023.6.11 添加一个ftp文件任务分发器,多台工作服务器接收分发器发送的需要拉取的文件路径,进行拉取
新增
    ftp_file_dispatcher.py 作为ftp文件任务分发器,需要单独运行在某台机器上,并需要配置工作服务器的相关信息
    ftp_processor.py 工作服务器上运行的ftp文件处理服务, 逻辑与之前的ftp_clien类似, 只是拉取目标变成了从任务队列ftp_fileq_xxx中获取
修改
    app.py 增加FtpFile接口,用来接收文件任务分发器发送的文件路径
    shared_variable.py 增加相关变量,ftp_fileq_http,ftp_fileq_email,ftp_fileq_ftp为用于处理ftp文件请求的全局任务队列; ftp_processors用来保存启动的ftp文件处理服务
    initializer.py 修改成初始化ftp_processor而不是ftp_client


2023.6.19 工作服务器修改成从配置文件file_types.txt中读取需要处理的文件类型, 
    同时将ftp_file_dispatcher ftp文件分发器的逻辑修改成按照worker_server_info.txt配置文件信息来对ftp文件分流

用法:
    在一台服务器上,单独放置ftp_file_dispatcher.py以及worker_server_info.txt,并运行python ftp_file_dispatcher.py
    在工作服务器上,配置file_types.txt,然后运行python app.py

2023.7.30 支持writer写日志时上传文件到s3存储上
