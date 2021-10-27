from flask import request, session
from flask_restx import Resource, Api, Namespace
from datetime import time, datetime

count = 1
Todo = Namespace('Post')


def get_curr_time():
    now = datetime.now()
    curr_time = now.strftime('%y-%m-%d %H:%M:%S')
    return curr_time

@Todo.route('')
class TodoPost(Resource):
    def post(self):
        try:
            global count

            idx = count
            count += 1
            datas = request.json.get('data')
            id = request.json.get('id')
            curr_time = get_curr_time()
            from app import db
            db.execute('''insert into post_info values(?,?,?,?,?)''', (id, idx, datas, curr_time, curr_time))
            # print(db.execute('''select * from post_info''').fetchall())
            return {
                'id': id,
                'post_no': idx,
                'data': datas,
                'created_date': curr_time,
                'modified_date': curr_time
            }, 200

        except:
            return {
                'message' : 'A login is required'
            }, 401

    def get(self):
        from app import db
        response = {'count' : 0, 'data' : []}
        offset, limit = request.args.get("offset"), request.args.get("limit")

        query_outputs = db.execute('''SELECT * FROM post_info LIMIT (?) OFFSET (?)''', (limit, offset)).fetchall()
        for output in query_outputs:
            dic = dict()
            id, post_number, data, created_date, modified_date = output
            dic['id'],dic['post_number'], dic['post'], dic['created_date'], dic['modified_date'] = id, post_number, data, created_date, modified_date
            response['data'].append(dic)
        response['count'] = len(response['data'])
        return response


@Todo.route('/<int:todo_id>')
class TodoSimple(Resource):
    # def get(self, todo_id):
    #     print(1)
    #     from app import db
    #     db.execute('''SELECT * FROM post_info LIMIT 10 OFFSET 10''')
    #     return {
    #         'todo_id': todo_id,
    #         'data': todos[todo_id]
    #     }

    def put(self, todo_id): # request message로 id
        user_id = request.json.get('id')
        post_number = request.json.get('post_no')
        datas = request.json.get('data')
        from app import db
        op = db.execute('''SELECT id,created_date FROM post_info where id =(?) and post_no =(?)''', (user_id, post_number)).fetchall()
        writer,created_time = op[0][0], op[0][1]

        if writer != user_id:
            return {
                'message' : "Your ID does not match the author's ID."
            }, 400

        modified_time = get_curr_time()
        db.execute('''UPDATE post_info SET data = (?), modified_date = (?) where id = (?) and post_no = (?)''', (datas, modified_time, user_id, post_number))
        # print(db.execute('''select * from post_info''').fetchall())
        return {
            'id': user_id,
            'post_no': post_number,
            'data': datas,
            'created_date': created_time,
            'modified_date': modified_time
        }, 200

    def delete(self, todo_id):
        user_id = request.json.get('id')
        post_number = request.json.get('post_no')

        from app import db
        op = db.execute('''SELECT id FROM post_info where id =(?) and post_no =(?)''',
                        (user_id, post_number)).fetchall()
        writer = op[0][0]

        if writer != user_id:
            return {
                'message' : "Your ID does not match the author's ID."
            }, 400


        db.execute('''DELETE FROM post_info where id = (?) and post_no = (?)''',
                   (user_id, post_number))
        # print(db.execute('''select * from post_info''').fetchall())
        return {
            "delete": "success"
        }, 200

