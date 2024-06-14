Bu depo, bir graf üzerindeki düğümler arasında Dijkstra algoritmasını kullanarak en kısa yolları hesaplayan ve bu yolları görselleştiren bir Python uygulamasıdır. Kullanıcı, belirli bir kaynak ve hedef düğümü girerek bu iki düğüm arasındaki en kısa yolu ve kaynak düğümden diğer tüm düğümlere olan en kısa yolları öğrenebilir. Uygulama ayrıca bu yolları grafiksel olarak da görselleştirmektedir.

Projede kullanılan graph.txt dosyası, grafın düğümleri arasındaki bağlantıları ve bu bağlantıların ağırlıklarını içerir. Her satırda iki düğüm ve aralarındaki bağlantının ağırlığı bulunur:
-İlk sütun, birinci düğümü (örneğin, A) belirtir.
-İkinci sütun, ikinci düğümü (örneğin, B) belirtir.
-Üçüncü sütun ise bu iki düğüm arasındaki bağlantının ağırlığını (örneğin, 2) temsil eder.
Kullanıcı bu graph.txt dosyasını kendi graf verilerine göre değiştirebilir ve özelleştirebilir.

Projede Kullanılan Kütüphaneler:
-networkx: Graf verilerini oluşturmak, işlemek ve analiz etmek için kullanılır. Dijkstra algoritması ve diğer grafik teorisi algoritmalarını içerir.
-matplotlib: Grafikleri çizmek ve görselleştirmek için kullanılır. Bu kütüphane ile grafın düğümleri, kenarları ve ağırlıkları görselleştirilebilir.

Çalıştırma:
-python main.py
-Terminalden kaynak ve hedef düğümleri girin

Çıktı:
![image](https://github.com/osmandemir2533/ShortestPathCalculationUsingDijkstra-sAlgorithm/assets/111290271/8e9f9bf1-8e58-4f2e-b96e-1c0ca7d4a037)
