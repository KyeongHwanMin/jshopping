### 필요
- Python 3.9.x

## 서버 구동 방법

### Python 종속성 설치
```bash
pip install -r requirements.txt
```
### MySQL 5.7 컨테이너 실행
```bash
docker-compose up -d
```
### DB마이그레이션
설계된 모델에 대한 스키마를 데이터베이스에 반영
```bash
python manage.py migrate
```
