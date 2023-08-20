## python 虚拟环境
python 3.11.3
安装 python -m venv .venv
激活 source .venv/bin/activate
关闭 deactivate 
生成依赖 pip freeze > requirements.txt/ 安装 pip install -r requirements.txt
vscode 选择 python 解释器 .venv

## 执行测试
vscode
或者 
命令行 pytest

## DDD 目录结构参考
ddd/
├── ddd/
│   ├── __init__.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   ├── entity1.py
│   │   │   ├── entity2.py
│   │   │   └── ...
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── repository1.py
│   │   │   ├── repository2.py
│   │   │   └── ...
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── service1.py
│   │       ├── service2.py
│   │       └── ...
│   ├── application/
│   │   ├── __init__.py
│   │   ├── use_cases/
│   │   │   ├── __init__.py
│   │   │   ├── use_case1.py
│   │   │   ├── use_case2.py
│   │   │   └── ...
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── service1.py
│   │   │   ├── service2.py
│   │   │   └── ...
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── repository1_impl.py
│   │   │   ├── repository2_impl.py
│   │   │   └── ...
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── service1_impl.py
│   │   │   ├── service2_impl.py
│   │   │   └── ...
│   │   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_domain/
│   │   ├── __init__.py
│   │   ├── test_entities.py
│   │   ├── test_repositories.py
│   │   └── test_services.py
│   ├── test_application/
│   │   ├── __init__.py
│   │   ├── test_use_cases.py
│   │   ├── test_services.py
│   │   └── ...
│   ├── test_infrastructure/
│   │   ├── __init__.py
│   │   ├── test_repositories.py
│   │   ├── test_services.py
│   │   └── ...
├── README.md
├── requirements.txt
├── setup.py
└── ...