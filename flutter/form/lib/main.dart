import 'package:flutter/material.dart';
import 'package:validators/validators.dart' as validator;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Form Demo'),
        ),
        body: TestForm(),
      ),
    );
  }
}

class TestForm extends StatefulWidget {
  @override
  _TestFormState createState() => _TestFormState();
}

class _TestFormState extends State<TestForm> {
  final _formKey = GlobalKey<FormState>();

  String _firstName;
  String _lastName;
  String _email;
  String _password1;
  String _password2;

  @override
  Widget build(BuildContext context) {
    final halfMediaWidth = MediaQuery.of(context).size.width / 2.0;

    return Form(
      key: _formKey,
      child: Column(
        children: <Widget>[
          Container(
            alignment: Alignment.topCenter,
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                Container(
                  alignment: Alignment.topCenter,
                  width: halfMediaWidth,
                  child: MyTextFormField(
                    hintText: 'First Name',
                    validator: (String value) {
                      if (value.isEmpty) {
                        return 'Enter your first name';
                      }
                      return null;
                    },
                    onSaved: (String value){
                      _firstName = value;
                    },
                  ),
                ),

                Container(
                  alignment: Alignment.topCenter,
                  width: halfMediaWidth,
                  child: MyTextFormField(
                    hintText: 'Last Name',
                    validator: (String value) {
                      if (value.isEmpty) {
                        return 'Enter your last name';
                      }
                      return null;
                    },
                    onSaved: (String value){
                      _lastName = value;
                    },
                  ),
                )
              ],
            ),
          ),

          MyTextFormField(
            hintText: 'Email',
            isEmail: true,
            validator: (String value) {
              if (!validator.isEmail(value)) {
                return 'Please enter a valid email';
              }
              return null;
            },
            onSaved: (String value){
              _email = value;
            },
          ),
          MyTextFormField(
            hintText: 'Password',
            isPassword: true,
            validator: (String value) {
              if (value.length < 7) {
                return 'Password should be minimum 7 characters';
              }

              _formKey.currentState.save();

              return null;
            },
            onSaved: (String value){
              _password1 = value;
            },
          ),
          MyTextFormField(
            hintText: 'Confirm Password',
            isPassword: true,
            validator: (String value) {
              if (value.length < 7) {
                return 'Password should be minimum 7 characters';
              }
              else if (_password1 != null && value != _password1) {
                print(value);
                print(_password1);
                return 'Password not matched';
              }

              return null;
            },
            onSaved: (String value){
              _password2 = value;
            },
          ),

          RaisedButton(
            color: Colors.blueAccent,
            onPressed: (){
              if (_formKey.currentState.validate()){
                _formKey.currentState.save();

                print(_firstName);
                print(_lastName);
                print(_email);
                print(_password1);
                print(_password2);

                Scaffold.of(context).showSnackBar(
                  SnackBar(
                    content: Text('Processing Data'),
                    backgroundColor: Colors.redAccent[100],
                  ),
                );
              }
            },
            child: Text(
              'Sign Up',
              style: TextStyle(
                color: Colors.white,
              ),
            ),

          )
        ],
      ),
    );
  }
}

class MyTextFormField extends StatelessWidget {
  final String hintText;
  final Function validator;
  final Function onSaved;
  final bool isPassword;
  final bool isEmail;

  MyTextFormField({
    this.hintText,
    this.validator,
    this.onSaved,
    this.isPassword = false,
    this.isEmail = false,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: TextFormField(
        decoration: InputDecoration(
          hintText: hintText,
          contentPadding: EdgeInsets.all(15.0),
          border: InputBorder.none,
          filled: true,
          fillColor: Colors.grey[200],
        ),
        obscureText: isPassword ? true : false,
        validator: validator,
        onSaved: onSaved,
        keyboardType: isEmail ? TextInputType.emailAddress : TextInputType.text,
      ),
    );
  }
}


