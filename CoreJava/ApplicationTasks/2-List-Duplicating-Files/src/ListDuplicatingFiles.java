import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ListDuplicatingFiles {
    public static void listDuplicatingFiles(File folder, List<File> result) throws IOException {
        File[] listOfFiles = folder.listFiles();
        for (int i = 0; i < listOfFiles.length; i++) {
            if (listOfFiles[i].isFile()) {
                boolean duplicate = false;
                byte[] f1 = Files.readAllBytes(listOfFiles[i].toPath());
                for (File file : result) {
                    byte[] f2 = Files.readAllBytes(file.toPath());
                    if (Arrays.equals(f1, f2))
                    {
                        duplicate = true;
                    }
                }
                if (!duplicate) {
                    result.add(listOfFiles[i]);
                }
            }
            if (listOfFiles[i].isDirectory()) {
                listDuplicatingFiles(listOfFiles[i], result);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        File startingPoint = new File("/home/stenly/TempStuff/TestDirectories/Test1");
        List<File> result = new ArrayList<File>();
        listDuplicatingFiles(startingPoint, result);
        for (File file : result) {
            System.out.println(file);
        }
    }
}
