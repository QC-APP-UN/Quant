/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package QuantForms;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

/**
 *
 * @author ngomezca
 */
public class PythonProcess implements Runnable{

    private String[] pathArray;
    
    public PythonProcess(String[] pathArray) {
        this.pathArray = pathArray;
    }

    @Override
    public void run() {
        
        String path = "";
        for(int i=0;i<this.pathArray.length;i++) path+=" "+this.pathArray[i];
        System.out.println(path); //Only in develop
        
        Process p;
        try {
            p = Runtime.getRuntime().exec(path);
            String stdin = null;
            String stderr = null;
            String input = "";
            String error = "";
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            BufferedReader err = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            
            
            while((stdin=in.readLine())!=null){
                input += stdin;
                System.out.println(stdin);
            }
            
            while((stderr=err.readLine())!=null){
                error +=stderr;
                System.out.println(stderr);
            }
            
            String [] msgerror=input.split(",");
            if(msgerror.length>1 && msgerror[msgerror.length-2].equals("ERROR"))
            JOptionPane.showMessageDialog(null, 
                              msgerror[msgerror.length-1], 
                              "Error", 
                              JOptionPane.WARNING_MESSAGE);
            
            
        } catch (IOException ex) {
            Logger.getLogger(PythonProcess.class.getName()).log(Level.SEVERE, null, ex);
        }
            
            
    }
    
}
