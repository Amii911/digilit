# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api

class UserList(Resource):
  def get(self):
          users = [user.to_dict() for user in User.query.all()]
          return jsonify(users)
      
  def post(self):
      form_json = request.get_json()
      new_user = User(username=form_json['username'], birthday=form_json['birthday'])
      
      # Hashes password and saves it to _password_hash
      new_user.password_hash = form_json['password']

      db.session.add(new_user)
      db.session.commit()
      session['user_id'] = new_user.id
      response = make_response(
          new_user.to_dict(),
          201
      )
      return response
  
api.add_resource(UserList, '/api/users', endpoint='users')

class Login(Resource):
    def post(self):
        try:
            request_json = request.get_json()
            username = request_json['username']
            password = request_json['password']
            user = User.query.filter_by(username=username).first()
            
            if user and user.authenticate(password):
                session['user_id'] = user.id
                response = make_response(user.to_dict(), 200)
                return response
            else:
                abort(401, "Incorrect username or password")
        except:
            abort(401, "Incorrect username or password")

api.add_resource(Login, '/api/login')

class Signup(Resource):
    def post(self):
        request_json = request.get_json()
        username = request_json.get('username')
        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return {'error': 'Username already exists'}, 409
        birthday = request_json.get('birthday')
        
        user = User(
            username=username,
            birthday=birthday
        )
        user.password_hash = request_json['password']

        try:
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return make_response(user.to_dict(), 201)
        except:
            return {'error': '422 Unprocessable Entity'}, 422

api.add_resource(Signup, '/api/signup')

class AuthorizedSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id=session['user_id']).first()
            response = make_response(
                user.to_dict(),
                200
            )
            return response
        except:
            abort(401, "Unauthorized")

api.add_resource(AuthorizedSession, '/api/authorized')

class Logout(Resource):
    def delete(self):
        session['user_id']=None 
        response = make_response('', 204)
        return response     
    
api.add_resource(Logout, '/api/logout')


@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

