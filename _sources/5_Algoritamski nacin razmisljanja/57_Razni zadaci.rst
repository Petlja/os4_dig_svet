Разни задаци
============

Сада имаш већ довољно искуства да самостално решаваш задатке. Кад год је могуће, реши задатак на више начина!

Како бисмо ти мало олакшали рад, убацили смо и две нове групе блокова: ``Гранање Карел`` и ``Петље Карел``. 
Блокови који се налазе у овим групама представљају комбинацију блокова из групе ``Петље``, 
``Гранање`` и ``Питај робота``. Слободно истражи и употреби блокове који ти највише одговарају! 

.. suggestionnote::

 **Када год је могуће и смислено, употреби одговарајуће петље у свом решењу!**

|

Задатак 1
---------

**Карел се нашао у уском пролазу. Помози му да узме обе лоптице!**

.. blockly-karel:: p561
  :categories: KarelCommands, Loops, KarelLoops, Branching
  
  {
      setup: function() {
           var world = new World(5, 5);
		   world.addNSWall(2, 1, 5)
		   world.addNSWall(3, 1, 5)
           world.setRobotStartAvenue(3);
           world.setRobotStartStreet(2);
           world.setRobotStartDirection("W");
           world.putBall(3, 5);
		   world.putBall(3, 1);
           var robot = new Robot();
           return {world: world, robot: robot};
      },
	  
      isSuccess: function(robot, world) {
          for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }           
   }


Задатак 2
---------

**Карел треба да убаци лоптицу у рупу!**

.. blockly-karel:: p562
  :categories: KarelCommands, Loops, KarelLoops, Branching
  
  {
      setup: function() {
           var world = new World(5, 5);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           world.putBall(4, 3);
		   world.putHole(5, 5);
           var robot = new Robot();
           return {world: world, robot: robot};
      },
	  
      isSuccess: function(robot, world) {
        for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }           
   }

Задатак 3
---------
  
**Карел треба да сакупи две лоптице. Да ли је кренуо на добру страну? Изабери краћи пут!**

.. blockly-karel:: p563
  :categories: KarelCommands, Loops, KarelLoops, Branching
  
  {
      setup: function() {
           var world = new World(5, 5);
		   world.addEWWall(2, 1, 3)
		   world.addNSWall(4, 2, 3)
		   world.addEWWall(2, 4, 3)
		   world.addNSWall(1, 2, 3)
           world.setRobotStartAvenue(3);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("W");
           world.putBall(5, 1);
		   world.putBall(5, 5);
           var robot = new Robot();
           
           return {world: world, robot: robot};
      },
	  
      isSuccess: function(robot, world) {
           return robot.getBalls() == 2;
      }
   }
      

Задатак 4
---------

**Помози Карелу да сакупи све лоптице са гомиле и врати се на поље (1, 1)!**

|
   
.. blockly-karel:: p564
  :categories: KarelCommands, Loops, KarelLoops, Branching
  
  {
      setup: function() {
           var world = new World(5, 5);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           world.putBalls(3, 1, 6);
		   world.addEWWall(1, 1, 5)
           var robot = new Robot();
           return {world: world, robot: robot};
      },
	  
      isSuccess: function(robot, world) {
        return robot.getAvenue() == 1 && 
		robot.getStreet() == 1 &&
        robot.getBalls() == 6;
		}
   }
   

Задатак 5
---------
  
**Помози Карелу да сакупи све лоптице и врати се на поље (1, 1).**

|
   
.. blockly-karel:: p565
  :categories: KarelCommands, Loops, KarelLoops, Branching
  
  {
      setup: function() {
           var world = new World(5, 5);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("N");
           world.putBalls(2, 1, 3);
		   world.putBalls(1, 2, 3);
		   world.putBalls(2, 2, 3);
           var robot = new Robot();
		   
           return {world: world, robot: robot};
      },
	  
      isSuccess: function(robot, world) {
	   return robot.getAvenue() == 1 && 
		robot.getStreet() == 1 &&
        robot.getBalls() == 9;
		}
           
   }
   
**Помоћ**: Уочи делове програма који се понављају!

Задатак 6
---------
  
**Задатак је сличан претходном. Карел треба да сакупи лоптице и убаци их у рупу која се налази на пољу (1, 1)**. 
Ако уочиш делове програма који се понављају, употреби петљу!

|
   
.. blockly-karel:: p566
  :categories: KarelCommands, Loops, KarelLoops, Branching
  
  {
      setup: function() {
           var world = new World(5, 5);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("N");
           world.putBall(2, 2);
		   world.putBall(2, 1);
		   world.putBall(1, 2);
		   world.putHoles(1, 1, 3);
           var robot = new Robot();

           return {world: world, robot: robot};
      },
	  
      isSuccess: function(robot, world) {
          for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }           
   }

Задатак 7
---------
 
**Карел треба да сакупи свих 12 лоптица.**

|

.. blockly-karel:: p567
  :categories: KarelCommands, Loops, Branching
  
  {
      setup: function() {
           var world = new World(5, 5);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("N");
		   world.putBalls(2, 2, 3);
		   world.putBalls(3, 2, 4);
		   world.putBalls(4, 2, 2);
		   world.putBalls(5, 2, 3);
           var robot = new Robot();
 
           return {world: world, robot: robot};
      },
	  
      isSuccess: function(robot, world) {
          for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }           
   }

**Помоћ**: Скрати састављање програма тако што ћеш користити петљу. 
На гомилама се налази различит број лопти. Да ли ће боље решење бити да користиш бројачку 
или условну петљу?

Карел прво треба да направи корак напред, па да скрене десно. Наредну групу корака треба да понови 
неколико пута: све док постоје лопте на пољу, узимај их, а затим направи корак напред како би прешао на следеће 
поље. И опет… све док постоје лопте на пољу, узимај их, а затим пређи на следеће поље… и опет… до када, 
колико пута? Можеш да приметиш која се група радњи понавља неколико пута. Када уочиш које су, стави их 
у одговарајућу петљу. 

|

Задатак 8
--------- 
 
**Карел је наишао на цик-цак зид. У сваком ћошку (углу) налази се лопта. Помози му да их све сакупи!**

| 

.. blockly-karel:: p568
  :categories: KarelCommands, Loops, KarelLoops, Branching
  
  {
      setup: function() {
           var world = new World(6, 6);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
		   for (var i = 1; i <= world.getAvenues()-1; i++)
		       world.addEWWall(i+1, i, 1)
		   for (var i = 1; i <= world.getAvenues()-1; i++){
		       world.addNSWall(i, i, 1)
		       world.putBall(i+1, i+1)
		  }
           var robot = new Robot();
           return {world: world, robot: robot};
      },
	  
      isSuccess: function(robot, world) {
          for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }           
   }

**Помоћ**: Као и у ранијим примерима, уочи које се наредбе понављају и стави их у петљу.

|

Задатак 9
---------

**Карел се тренутно налази код рупе у коју треба да убаци три лопте. Помози му да то уради!**
 
Како би увежбао примену бројачких петљи, условних петљи и гранања у програму, покушај овај задатак 
да решиш на више различитих начина! 

|

.. blockly-karel:: p569
  :categories: KarelCommands, Loops, KarelLoops, Branching
  
  {
      setup: function() {
           var world = new World(5, 5);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           world.putBall(5, 1);
		   world.putBall(5, 5);
		   world.putBall(1, 5);
		   world.putHoles(1, 1, 3);
           var robot = new Robot();
           
           return {world: world, robot: robot};
      },
	  
      isSuccess: function(robot, world) {
          for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }           
   }

|

Задатак 10
----------

**Ова оптица се баш сакрила! Помози Карелу да стигне до ње и узме је!**
 
.. blockly-karel:: p5610
  :categories: KarelCommands, Loops, KarelLoops, Branching
  
  {
      setup: function() {
           var world = new World(6, 6);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           world.putBall(1, 2);
		   world.addEWWall(1, 1, 5)
		   world.addEWWall(2, 5, 4)
		   world.addNSWall(1, 2, 4)
		   world.addNSWall(5, 2, 4)
           var robot = new Robot();
           return {world: world, robot: robot};
      },
	  
      isSuccess: function(robot, world) {
	      for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }           
   }
   
**Помоћ**: Карел треба да иде напред док не наиђе на зид (док може напред). Када дође до зида, 
треба да скрене лево. Колико пута треба да понови овај поступак? Када стигне на последње поље, 
треба да узме лопту и задатак ће бити решен!  

