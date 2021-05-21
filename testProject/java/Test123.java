import sun.misc.BASE64Encoder;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.sql.Timestamp;


public class Test123 {

    public static void main(String[] args) throws Exception {
        String url = "xxxxxxx/api/publicAPIService/updateMemberAcount";
//        long tim=System.currentTimeMillis();
        long time = 1608515670794L;
        Timestamp time1 = new Timestamp(time);
        String appKey = "bdba74e057c445baad9827aded239cb4";
        String appSecret = "aced1c7135aa4952a700fa7f521613d0";
        String signature = getHmacSHA1(time1 + appKey, appSecret);
        System.out.println("appKey:" + appKey);
        System.out.println("timestamp:" + time1.toString());
        System.out.println("signature:" + signature);

        String signature2 = getHmacSHA1("2020-12-21 9:54:30.794" + appKey , appSecret);
        System.out.println("appKey:" + appKey);
        System.out.println("timestamp2: 2020-12-21 9:54:30.794");
        System.out.println("signature2:" + signature2);
    }


    public static String getHmacSHA1(String message, String key) throws UnsupportedEncodingException, NoSuchAlgorithmException, InvalidKeyException {
        String hmacSha1 = null;
        message = URLEncoder.encode(message, "UTF-8");
        //message = "2020-12-21+9%3a54%3a30.794bdba74e057c445baad9827aded239cb4";
        System.out.println("message " + message );
        Mac mac = Mac.getInstance("HmacSHA1");
        SecretKeySpec spec = new SecretKeySpec(key.getBytes(), "HmacSHA1");
        mac.init(spec);
        byte[] byteHMAC = mac.doFinal(message.getBytes());
        hmacSha1 = new BASE64Encoder().encode(byteHMAC);
        return hmacSha1;
    }
}

