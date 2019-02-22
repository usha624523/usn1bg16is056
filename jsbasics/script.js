/*
//decision making
var age=18;
if (age<13){
    console.log("minor");
}else if (age >= 18){
    console.log("major")
}

//con?true:false
age>=18?console.log("major"):console.log("minor");
*/
//function
/*function uk(fname,lname){
    console.log(fname+' '+lname);
}
uk('deepti','agarwal');

//array
var names=["uk","ankita","pragya"];
console.log(names[2]);
console.log(names.length);
names.push("khushi");
names.unshift("raj");
names.pop();
console.log(names);
*/
//challenge2
//var tip=["9.8","18.6","26.8"];
//var bill=["57.8","142.6","294.8"];
var bill=[48,124,268];
var tip=[0,0,0];
var amt=[0,0,0];
for(i=0;i<bill.length;i++){
    if(bill[i]<50){
        tip[i]=0.2*bill[i];
        amt[i]=tip[i]+bill[i];
    }
     else if((bill[i]>50 && bill[i]<200)){
        tip[i]=0.15*bill[i];
        amt[i]=tip[i]+bill[i];
    }

    else {
        tip[i]=0.1*bill[i];
        amt[i]=tip[i]+bill[i];
      }
    }
    console.log(tip);
    console.log(amt);
 
    /*var myDetails={
        fname:'usha',
        lname:'kiran',
        dob:2001,
        family: ['prabhat','sonali'],
        calcAge: function(birthYear){
            return 2019-birthYear;
        }
    }
    console.log(myDetails.fname);
    var z='dob';
    console.log(myDetails[z]);

    myDetails.dob=1981;
    console.log(myDetails);
//new object

var shiva = new Object();
shiva.fname='vivek';
console.log(shiva);

console.log('vivek is'+myDetails.calcAge(2001)+'years old');*/

