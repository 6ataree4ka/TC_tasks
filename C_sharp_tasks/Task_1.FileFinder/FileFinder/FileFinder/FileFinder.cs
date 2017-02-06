using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace FileFinder
{
    class FileFinder
    {
        static void Main(string[] args)
        {
            string targetPath = "";

            do
            {
                Console.WriteLine("Enter path to folder: ");
                string path = Console.ReadLine().Trim();
                if (Directory.Exists(path))
                {
                    if (path.EndsWith(":"))
                    {
                        targetPath = path + "\\";
                    }
                    else
                    {
                        targetPath = path;
                    }
                }
                else
                {
                    Console.WriteLine("'{0}' is not a valid directory.", path);
                }
            }
            while (targetPath == "");

            string targetExt = "";

            do
            {
                Console.WriteLine("Enter file extension: ");
                string ext = Console.ReadLine().Replace(" ", string.Empty);
                if (ext == "")
                {
                    Console.WriteLine("File extension can't be empty.");
                }
                else
                {
                    targetExt = ext;
                }
            }
            while (targetExt == "");

            // Create empty dictiionary where key = filename, value = creation date
            Dictionary<string, DateTime> filesWithCreationDate = new Dictionary<string, DateTime>();

            // Mask *.ext is used to find files only with a needed extension
            string[] files = Directory.GetFiles(targetPath, ("*." + targetExt));
            if (files.Length == 0)
            {
                Console.WriteLine("There are no *.{0} files in {1} folder.", targetExt, targetPath);
                Console.ReadLine();
            }
            else
            {
                foreach (string file in files)
                {
                    string fileName = Path.GetFileName(file);
                    DateTime creationTime = File.GetCreationTime(file);
                    filesWithCreationDate.Add(fileName, creationTime);
                }

                // Sort dictionary by descending
                filesWithCreationDate = filesWithCreationDate.OrderByDescending(x => x.Value).ToDictionary(x => x.Key, x => x.Value);
                KeyValuePair<string, DateTime> newest = filesWithCreationDate.First();

                Console.WriteLine("The newest file(s):");
                int time = 10;
                foreach (KeyValuePair<string, DateTime> item in filesWithCreationDate)
                {
                    if ((newest.Value - item.Value).TotalSeconds <= time)
                    {
                        Console.WriteLine("{0}, creation date is {1}.", item.Key, item.Value);
                    }
                }
                Console.ReadLine();
            }
        }
    }
}