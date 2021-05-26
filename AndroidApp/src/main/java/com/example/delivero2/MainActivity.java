package com.example.delivero2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import com.google.android.material.snackbar.Snackbar;

import java.io.Console;
import java.util.Dictionary;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.List;

public class MainActivity extends AppCompatActivity
{
    public static final String EXTRA_MESSAGE = "com.example.myfirstapp.MESSAGE";
    public static final int REGISTER_ACTIVITY_REQUEST_CODE = 0;
    Hashtable<String, String> Users = new Hashtable<String, String>();

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void Login(View view)
    {
        Users.put("Raul", "pizza");
        Users.put("User1", "pass1");
        Users.put("User2", "pass2");
        Users.put("User3", "pass3");
        Users.put("User4", "pass4");
        Users.put("User5", "pass5");
        Users.put("User6", "pass6");
        Users.put("User7", "pass7");

        //Intent intent = new Intent(this, DisplayMessageActivity.class);
        Intent intent = new Intent(this, MapsActivity.class);
        EditText editText = (EditText) findViewById(R.id.editTextTextPersonName);
        EditText editText_password = (EditText) findViewById(R.id.editTextTextPassword);

        Snackbar mySnackbar = Snackbar.make(view, "Failed to login", 2000);

        String user_name = editText.getText().toString();
        String password = editText_password.getText().toString();
        String message = "Login successful";

        String pass = Users.get(user_name);

        if(pass != null && pass.equals(password))
        {
           //intent.putExtra(EXTRA_MESSAGE, message);
            startActivity(intent);
        }
        else
        {
            mySnackbar.show();
        }
    }

    public void Register(View view)
    {
        Intent intent = new Intent(this, Register_User.class);
        startActivityForResult(intent, REGISTER_ACTIVITY_REQUEST_CODE);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data)
    {
        super.onActivityResult(requestCode, resultCode, data);

        if(requestCode == REGISTER_ACTIVITY_REQUEST_CODE)
        {
            if(resultCode == RESULT_OK)
            {
                String newUser = data.getStringExtra("userName");
                String newPass = data.getStringExtra("password");
                Users.put(newUser, newPass);
            }
        }
    }
}