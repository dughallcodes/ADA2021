package com.example.delivero2;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class Register_User extends AppCompatActivity
{

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register__user);
    }

    public void addUser(View view)
    {
        Intent intent = new Intent();

        EditText user = (EditText) findViewById(R.id.new_user);
        EditText set_password = (EditText) findViewById(R.id.Set_Password);
        EditText conf_password = (EditText) findViewById(R.id.Confirm_Password);

        String user_name = user.getText().toString();
        String password_set = set_password.getText().toString();
        String password_conf = conf_password.getText().toString();

        if(user_name.isEmpty())
        {
            alertDialog("User is empty");
        }
        else if(password_set.isEmpty())
        {
            alertDialog("Password is empty");
        }
        else if(!password_set.equals(password_conf))
        {
            alertDialog("Passwords don't match");
        }
        else
        {
            intent.putExtra("userName", user_name);
            intent.putExtra("password", password_set);
            setResult(RESULT_OK, intent);
            finish();
        }

    }

    private void alertDialog(String error)
    {
        AlertDialog.Builder dialog=new AlertDialog.Builder(this);
        dialog.setMessage(error);
        dialog.setTitle("Error");
        dialog.setPositiveButton("YES",
                new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog,
                                        int which) {
                        Toast.makeText(getApplicationContext(),"Yes is clicked", Toast.LENGTH_LONG).show();
                    }
                });
        dialog.setNegativeButton("cancel",new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                Toast.makeText(getApplicationContext(),"cancel is clicked",Toast.LENGTH_LONG).show();
            }
        });
        AlertDialog alertDialog=dialog.create();
        alertDialog.show();
    }
}