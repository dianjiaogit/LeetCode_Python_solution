import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class ElephantDescription {
    public String name;
    public int height;
}

class ElephantSchedule {
    public String name;
    public int enterTime;
    public int exitTime;
}

class ElephantCompetition {
    List<ElephantDescription> elephants;
    List<ElephantSchedule> schedule;
    List<ElephantDescription> our_elephants_in_competition;
    List<Integer> other_elephants_in_competition;
    
    public ElephantCompetition(List<ElephantDescription> elephants, List<ElephantSchedule> schedule) {
        this.elephants = elephants;
        this.schedule = schedule;
        this.our_elephants_in_competition = new ArrayList<ElephantDescription>();
        this.other_elephants_in_competition = new ArrayList<Integer>();
    }

    public void elephantEntered(int currentTime, int height) {
        /* Enter your code here. */
        Boolean added = false;
        for (int i = 0; i < schedule.size(); i++) {
            for (int j = 0; j < elephants.size(); j++) {
                if (schedule.get(i).enterTime == currentTime) {     
                    if (schedule.get(i).name.equals(elephants.get(j).name)) {
                        if (elephants.get(j).height == height) {
                            our_elephants_in_competition.add(elephants.get(j));
                            elephants.remove(j);
                            added = true;
                            break;
                        }
                    }
                }
            }
        }
        if (!added) {
            other_elephants_in_competition.add(height);
        }
    }

    public void elephantLeft(int currentTime, int height) {
        /* Enter your code here. */
        Boolean lefted = false;
        for (int i = 0; i < our_elephants_in_competition.size(); i++) {
            if (our_elephants_in_competition.get(i).height == height) {
                for (int j = 0; j < schedule.size(); j++) {
                    if (our_elephants_in_competition.get(i).name.equals(schedule.get(j).name) && schedule.get(j).exitTime == currentTime) {
                        our_elephants_in_competition.remove(i);
                        lefted = true;
                        break;
                    }
                }
            }
        }
        if (!lefted) {
            for (int i = 0; i < other_elephants_in_competition.size(); i++) {
                if (other_elephants_in_competition.get(i) == height) {
                    other_elephants_in_competition.remove(i);
                }
            }
        }
    }

    public List<String> getBiggestElephants()
    {
        /* Enter your code here. */
        List<ElephantDescription> our_biggest_Elephants = new ArrayList<ElephantDescription>();
        Integer max_others;
        if (other_elephants_in_competition.size() > 0) {
            max_others = Collections.max(other_elephants_in_competition);
        }
        else {
            max_others = 0;
        }
        for (int i = 0; i < our_elephants_in_competition.size(); i++) {
            if (our_elephants_in_competition.get(i).height >= max_others) {
                our_biggest_Elephants.add(our_elephants_in_competition.get(i));
            }
        }
        List<String> names = new ArrayList<String>();
        if (our_biggest_Elephants.size() > 0) {
            for (int i = 0; i < our_biggest_Elephants.size(); i++) {
                names.add(our_biggest_Elephants.get(i).name);
            }
        }
        return names;
    }
}

public class Solution {
    public static void main(String args[]) throws Exception {
        Scanner scanner = new Scanner(System.in);
        String operation;

        List<ElephantDescription> descriptions = new ArrayList<ElephantDescription>();
        List<ElephantSchedule> schedule = new ArrayList<ElephantSchedule>();

        do
        {
            operation = scanner.next();

            if (operation.equals("definition"))
            {
                ElephantDescription description = new ElephantDescription();
                description.name = scanner.next();
                description.height = scanner.nextInt();

                descriptions.add(description);
            }
            if (operation.equals("schedule"))
            {
                ElephantSchedule scheduleEntry = new ElephantSchedule();
                scheduleEntry.name = scanner.next();
                scheduleEntry.enterTime = scanner.nextInt();
                scheduleEntry.exitTime = scanner.nextInt();

                schedule.add(scheduleEntry);
            }
        } while (!operation.equals("start"));

        ElephantCompetition elephantCompetition = new ElephantCompetition(descriptions, schedule);

        do
        {
            int currentTime = scanner.nextInt();
            operation = scanner.next();

            if (operation.equals("enter"))
            {
                int size = scanner.nextInt();

                elephantCompetition.elephantEntered(currentTime, size);
            }
            if (operation.equals("exit"))
            {
                int size = scanner.nextInt();

                elephantCompetition.elephantLeft(currentTime, size);
            }
            if (operation.equals("inspect"))
            {
                List<String> elephants = elephantCompetition.getBiggestElephants();

                System.out.print(elephants.size());

                for (String name : elephants) {
                    System.out.print(" " + name);
                }

                System.out.println();
            }
        } while (!operation.equals("end"));
    }
}