import java.io.File;
import java.io.FileFilter;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class ListDuplicatingFiles {
    public static void getAllFiles(File folder, List<File> result) {
        File[] listOfFiles = folder.listFiles();
        for (int i = 0; i < listOfFiles.length; i++) {
            if (listOfFiles[i].isFile()) {
               result.add(listOfFiles[i]);
            }
            if (listOfFiles[i].isDirectory()) {
                getAllFiles(listOfFiles[i], result);
            }
        }
    }

    public static void getUniqueFiles(List<File> allFiles, List<File> uniqueFiles) throws IOException {
        for (int i = 0; i < allFiles.size(); i++) {
            boolean duplicate = false;
            byte[] f1 = Files.readAllBytes(allFiles.get(i).toPath());
            for (File file : uniqueFiles) {
                byte[] f2 = Files.readAllBytes(file.toPath());
                if (Arrays.equals(f1, f2))
                {
                    duplicate = true;
                }
            }
            if (!duplicate) {
                uniqueFiles.add(allFiles.get(i));
            }
        }
    }

    public static void main(String[] args) throws Exception {
        File startingPoint = new File("/home/stenly/TempStuff/TestDirectories");
        List<File> allFiles = new ArrayList<File>();
        getAllFiles(startingPoint, allFiles);

        List<File> uniqueFiles = new ArrayList<File>();
        getUniqueFiles(allFiles, uniqueFiles);
        for (File file : uniqueFiles) {
            System.out.println(file);
        }
    }
}
