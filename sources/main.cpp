#include <fstream>
#include <iostream>
#include <openssl/bn.h>
#include <openssl/crypto.h>
#include <sstream>
#include <string>

std::string add(const char * a, const char * b) {
    BIGNUM *bn1 = NULL;
    BIGNUM *bn2 = NULL;

    BN_CTX *ctx = BN_CTX_new();

    BN_dec2bn(&bn1, a); // convert the string to BIGNUM
    BN_dec2bn(&bn2, b);

    BN_add(bn1, bn1, bn2); // bn1 = bn1 + bn2

    char *result_str = BN_bn2dec(bn1);  // convert the BIGNUM back to string
    std::string ret_val = result_str;
    OPENSSL_free(result_str);

    BN_free(bn1);
    BN_free(bn2);
    BN_CTX_free(ctx);
    return ret_val;
}

int main(void) {
    std::ifstream in("test.txt");
    std::string line;
    std::string res("0");
    while (std::getline(in, line)) {
        res = add(res.c_str(),line.c_str());
    }
    std::cout << res << std::endl;
}
